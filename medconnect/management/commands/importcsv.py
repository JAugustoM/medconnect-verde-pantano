import pandas as pd
from django.core.management.base import BaseCommand, CommandError
from medconnect.models import Hospital

class Command(BaseCommand):

    help = "Imports .csv file data to Hospital"

    def add_arguments(self, parser):
        parser.add_argument('path')
        parser.add_argument('uf')
        parser.add_argument(
            '--display',
            action='store_true'
        )
        parser.add_argument(
            '--delete',
            action='store_true'
        )
    
    def handle(self, *args, **options):
        df = pd.read_csv(options['path'])
        df = df.fillna('')

        if options['uf'] != '*':
            df = df[df["UF"] == options['uf']]
            df = df.reset_index(drop=True)

        df = df[df["COMP"] == df["COMP"].max()]

        if options['display']:
            entries = 0

            print(df['COMP'].value_counts())

            for i in range(0, len(df.index)):

                if df['NO_COMPLEMENTO'].iloc[i] == '':
                    self.stdout.write(self.style.SUCCESS(f"{df['NO_LOGRADOURO'].iloc[i]}" + f" {df['NU_ENDERECO'].iloc[i]}" + f" - {df['NO_BAIRRO'].iloc[i]}"))
                else:
                    self.stdout.write(self.style.SUCCESS(f"{df['NO_LOGRADOURO'].iloc[i]}" + f" {df['NO_COMPLEMENTO'].iloc[i]}" + f" {df['NU_ENDERECO'].iloc[i]}" + f" - {df['NO_BAIRRO'].iloc[i]}"))
                
                entries += 1

            self.stdout.write(self.style.SUCCESS(f"Entries: {entries}"))

        if options['delete']:
            Hospital.objects.filter(uf__exact=options["uf"]).delete()

        else:
            created = 0
            updated = 0
            conectivos = ('de', 'da', 'das', 'do', 'dos', 'e')

            for i in range(0, len(df.index)):

                if df['NO_COMPLEMENTO'].iloc[i] == '':
                    strings = f"{df['NO_LOGRADOURO'].iloc[i]}" + f" {df['NU_ENDERECO'].iloc[i]}" + f" - {df['NO_BAIRRO'].iloc[i]}"
                    strings = strings.lower().split()
                else:
                    strings = f"{df['NO_LOGRADOURO'].iloc[i]}" + f" {df['NO_COMPLEMENTO'].iloc[i]}" + f" {df['NU_ENDERECO'].iloc[i]}" + f" - {df['NO_BAIRRO'].iloc[i]}"
                    strings = strings.lower().split()

                endereco = ""

                for temp in strings:
                    if temp not in conectivos:
                        temp = temp.capitalize()
                    endereco = endereco + temp
                    endereco = endereco + " "
                endereco = endereco.strip()

                cnes = f"{df['CNES'].iloc[i]}"

                strings = f"{df['NOME_ESTABELECIMENTO'].iloc[i]}".lower().split()
                nome = ""
                for temp in strings:
                    if temp not in conectivos:
                        temp = temp.capitalize()
                    nome = nome + temp
                    nome = nome + " "
                nome = nome.strip()

                # print(nome)

                cep = df['CO_CEP'].iloc[i]
                categoria = df['DESC_NATUREZA_JURIDICA'].iloc[i]
                uf = df['UF'].iloc[i]

                strings = f"{df['MUNICIPIO'].iloc[i]}".lower().split()
                municipio = ""
                for temp in strings:
                    if temp not in conectivos:
                        temp = temp.capitalize()
                    municipio = municipio + temp
                    municipio = municipio + " "
                municipio = municipio.strip()

                # print(municipio)

                telefone = df["NU_TELEFONE"].iloc[i]
                if telefone == '':
                    telefone = "Telefone não informado"

                email = df["NO_EMAIL"].iloc[i]
                if email == '':
                    email = "Email não informado"

                leitos = df["LEITOS_EXISTENTES"].iloc[i]
                uti_adulto = df["UTI_ADULTO_EXIST"].iloc[i]
                uti_pediatrico = df["UTI_PEDIATRICO_EXIST"].iloc[i]
                uti_neonatal = df["UTI_NEONATAL_EXIST"].iloc[i]
                uti_queimado = df["UTI_QUEIMADO_EXIST"].iloc[i]

                obj, create = Hospital.objects.update_or_create(
                    cnes=cnes,
                    defaults={
                        "nome":nome,
                        "endereco":endereco,
                        "cep":cep,
                        "categoria":categoria,
                        "uf":uf,
                        "municipio":municipio,
                        "telefone":telefone,
                        "email":email,
                        "leitos":leitos,
                        "uti_adulto":uti_adulto,
                        "uti_pediatrico":uti_pediatrico,
                        "uti_neonatal":uti_neonatal,
                        "uti_queimado":uti_queimado
                    }            
                )

                if create == True:
                    created += 1

                else:
                    updated += 1

            self.stdout.write(self.style.SUCCESS(f"Created: {created}"))
            self.stdout.write(self.style.SUCCESS(f"Updated: {updated}"))
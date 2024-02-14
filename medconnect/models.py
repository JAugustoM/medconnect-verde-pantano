from django.db import models

from django.db import models
from django.utils import timezone
from datetime import date, timedelta
from django.contrib.auth.models import User

class Hospital(models.Model):

    class Meta:
        verbose_name_plural = "Hospitais"

    CATEGORIAS = [
        ("HOSPITAL_PUBLICO", "Público"),
        ("HOSPITAL_PRIVADO", "Privado"),
        ("HOSPITAL_FILANTROPICO", "Filantrópico")
    ]

    UFS = [
        ("AC","Acre"),
        ("AL","Alagoas"),
        ("AP","Amapá"),
        ("AM","Amazonas"),
        ("BA","Bahia"),
        ("CE","Ceará"),
        ("DF","Distrito Federal"),
        ("ES","Espirito Santo"),
        ("GO","Goiás"),
        ("MA","Maranhão"),
        ("MT","Mato Grosso"),
        ("MS","Mato Grosso do Sul"),
        ("MG","Minas Gerais"),
        ("PA","Pará"),
        ("PB","Paraíba"),
        ("PR","Paraná"),
        ("PE","Pernambuco"),
        ("PI","Piauí"),
        ("RJ","Rio de Janeiro"),
        ("RN","Rio Grande do Norte"),
        ("RS","Rio Grande do Sul"),
        ("RO","Rondônia"),
        ("RR","Roraima"),
        ("SC","Santa Catarina"),
        ("SP","Sâo Paulo"),
        ("SE","Sergipe"),
        ("TO","Tocantins")
    ]

    cnes = models.CharField(max_length=7, null=False, blank=False, primary_key=True, default="0000000", editable=False)
    nome = models.CharField(max_length=100, null=False, blank=False)
    endereco = models.CharField(max_length=150, null=False, blank=False)
    cep = models.CharField(max_length=20, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=CATEGORIAS, default='')
    uf = models.CharField(max_length=100, choices=UFS, default='')
    municipio = models.CharField(max_length=150,  default='')
    telefone = models.CharField(max_length=100, null=False, blank=False, default="Não informado")
    email = models.CharField(max_length=100, null=False, blank=False, default="Não informado")
    tempo_emergente = models.IntegerField(null=False, blank=False, default=0)
    tempo_muito_urgente = models.IntegerField(null=False, blank=False, default=0)
    tempo_urgente = models.IntegerField(null=False, blank=False, default=0)
    tempo_pouco_urgente = models.IntegerField(null=False, blank=False, default=0)
    tempo_nao_urgente = models.IntegerField(null=False, blank=False, default=0)
    nota = models.DecimalField(max_digits=4, decimal_places=3, null=False, blank=False, default=0)
    leitos = models.IntegerField(null=False, blank=False, default=0)
    uti_adulto = models.IntegerField(null=False, blank=False, default=0)
    uti_pediatrico = models.IntegerField(null=False, blank=False, default=0)
    uti_neonatal = models.IntegerField(null=False, blank=False, default=0)
    uti_queimado = models.IntegerField(null=False, blank=False, default=0)
    atualizacao = models.DateTimeField(null=False, blank=False, default=timezone.now)

    def __str__(self):
        return self.nome

class Avaliacao(models.Model):

    class Meta:
        verbose_name = "avaliação"
        verbose_name_plural = "Avaliações"

    RISCO = [
        ("EMERGENTE", "Emergente"),
        ("MUITO_URGENTE", "Muito Urgente"),
        ("URGENTE", "Urgente"),
        ("POUCO_URGENTE", "Pouco Urgente"),
        ("NAO_URGENTE", "Não Urgente")
    ]

    usuario = models.CharField(max_length=100, null=False, blank=False, default="")
    numero = models.IntegerField(null=False, blank=False, default=1)
    data = models.DateTimeField(null=False, blank=False, default=timezone.now)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    risco = models.CharField(max_length=100, null=False, blank=False, default="NAO_URGENTE", choices=RISCO)
    horario_entrada = models.DateTimeField(null=False, blank=False, default=timezone.now)
    horario_atendimento = models.DateTimeField(null=False, blank=False, default=timezone.now)
    horario_saida = models.DateTimeField(null=False, blank=False, default=timezone.now)
    duracao = models.DurationField(null=False, blank=False, default=timedelta(minutes=30))
    avaliacao = models.IntegerField(null=False, blank=False, default=3)
    observacao = models.TextField(null=False, blank=False, default="")

    def __str__(self):
        return self.risco

class Dados(models.Model):

    class Meta:
        verbose_name = "dados"
        verbose_name_plural = "Dados"

    GENERO = [
        ("na","Não informado"),
        ("homem-cis", "Homem cis"),
        ("homem-trans", "Homem trans"),
        ("mulher-cis", "Mulher cis"),
        ("mulher-trans", "Mulher trans"),
        ("nao-binario", "Não-binário"),
        ("outro", "Outro")
    ]

    TIPO_SANGUINIO = [
        ("A+","A+"),
        ("A-","A-"),
        ("B+","B+"),
        ("B-","B-"),
        ("AB+","AB+"),
        ("AB-","AB-"),
        ("O+","O+"),
        ("O-","O-"),
        ("na","Não informado/Não sabe")
    ]

    FREQUENCIA = [
        ("n","Não"),
        ("d","Diariamente"),
        ("s","Semanalmente"),
        ("m","Mensalmente"),
        ("a","Anualmente")
    ]

    usuario = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    data_nascimento = models.DateField(null=False, blank=False, default=timezone.now)
    genero = models.CharField(max_length=20, null=False, blank=False, default="na", choices=GENERO)
    profissao = models.CharField(max_length=200, null=False, blank=False, default="Não informada")
    endereco = models.CharField(max_length=200, null=False, blank=False, default="Não informado")
    telefone = models.CharField(max_length=20, null=False, blank=False, default="Não informado")
    peso = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False, default=0)
    altura = models.DecimalField(max_digits=3, decimal_places=2, null=False, blank=False, default=0)
    tipo_sanguineo = models.CharField(max_length=4, null=False, blank=False, default="na", choices=TIPO_SANGUINIO)
    fumo_alcool = models.CharField(max_length=200, null=False, blank=False, default="n", choices=FREQUENCIA)
    exercicio = models.CharField(max_length=200, null=False, blank=False, default="Nâo informado")
    exercicio_frequencia = models.CharField(max_length=200, null=False, blank=False, default="n", choices=FREQUENCIA)

    def __str__(self):
        return self.usuario.username

class Doencas(models.Model):

    class Meta:
        verbose_name = "doença"
        verbose_name_plural = "Doenças"

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="doencas")
    doenca = models.CharField(max_length=200, null=False, blank=False, default="N/A")

    def __str__(self):
        return self.doenca

class Sintomas(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sintomas")
    sintoma = models.CharField(max_length=200, null=False, blank=False, default="N/A")

    def __str__(self):
        return self.sintoma

class Diagnostico(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="diagnosticos")
    diagnostico = models.CharField(max_length=200, null=False, blank=False, default="N/A")

    def __str__(self):
        return self.diagnostico

class Cirurgia(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cirurgias")
    cirurgia = models.CharField(max_length=200, null=False, blank=False, default="N/A")
    data = models.DateField(null=False, blank=False, default=timezone.now)

    def __str__(self):
        return self.cirurgia

class Internacao(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="internacoes")
    internacao = models.CharField(max_length=200, null=False, blank=False, default="N/A")
    tempo = models.IntegerField(null=False, blank=False, default=0)
    data = models.DateField(null=False, blank=False, default=timezone.now)

    def __str__(self):
        return self.internacao

class Condicao_familiar(models.Model):

    GRAU_PARENTESCO = [
        ("1", "1° Grau"),
        ("2", "2° Grau"),
        ("3", "3° Grau")
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="condicao_familiar")
    condicao = models.CharField(max_length=200, null=False, blank=False, default="N/A")
    grau_parentesco = models.CharField(max_length=10, null=False, blank=False, default="1", choices=GRAU_PARENTESCO)

    def __str__(self):
        return self.condicao

class Medicamento(models.Model):

    TIPO_MEDICAMENTO = [
        ("1", "Medicamento com prescrição"),
        ("2", "Medicamento sem prescrição")
    ]

    FREQUENCIA = [
        ("n","Não"),
        ("d","Diariamente"),
        ("s","Semanalmente"),
        ("m","Mensalmente"),
        ("a","Anualmente")
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="medicamentos")
    tipo = models.CharField(max_length=200, null=False, blank=False, default="1", choices=TIPO_MEDICAMENTO)
    medicamento = models.CharField(max_length=200, null=False, blank=False, default="N/A")
    frequencia = models.CharField(max_length=200, null=False, blank=False, default="n", choices=FREQUENCIA)
    numero_frequencia = models.IntegerField(null=False, blank=False, default=0)

    def __str__(self):
        return self.medicamento
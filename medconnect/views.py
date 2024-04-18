from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from setup import settings
from urllib.parse import urlparse
from .models import Hospital, Avaliacao, Dados, Doencas, Sintomas, Diagnostico, Cirurgia, Internacao, Condicao_familiar, Medicamento
from .forms import BuscarForms, FilterForms
from bs4 import BeautifulSoup
import requests
import json

def index(request):

    news_url = "https://g1.globo.com/bemestar/"
    response = requests.get(news_url)
    news_website = BeautifulSoup(response.text, "html.parser")

    titles = news_website.find_all('h2')
    links = news_website.find_all('a', class_="feed-post-link gui-color-primary gui-color-hover")
    images = news_website.find_all('img', class_="bstn-fd-picture-image")
    summaries = news_website.find_all('div', class_="feed-post-body-resumo")

    h2_texts = [title.text for title in titles] 
    src_values = [image.get('src') for image in images]
    href_values = [link.get('href') for link in links]
    p_texts = [summary.text for summary in summaries]

    news_data = list(zip(h2_texts, src_values, p_texts, href_values))
    hospitais = Hospital.objects.order_by("-nota")[:8]
    buscar2 = BuscarForms()
    filter_form = FilterForms()
    counter = (1, 2, 3, 4, 5)

    context = {"news_data": news_data,
               "hospitais": hospitais, 
               "buscar": buscar2, 
               "filter":filter_form, 
               "counter":counter}

    return render(request, 'medconnect/index.html', context)

def locais_de_atendimento(request):
    hospitais = Hospital.objects.order_by("nome")
    buscar2 = BuscarForms()
    filter_form = FilterForms()
    context = {"hospitais": hospitais, "buscar": buscar2, "filter":filter_form}

    return render(request, 'medconnect/locaisdeatendimento.html', context)

def buscar(request):
    hospitais = Hospital.objects.order_by("nome")
    buscar2 = BuscarForms()
    filter_form = FilterForms()

    if "uf" in request.GET:
        uf_a_buscar = request.GET['uf']

        if uf_a_buscar:
            hospitais = hospitais.filter(uf__iexact=uf_a_buscar)

    if "municipio" in request.GET:
        municipio_a_buscar = request.GET['municipio']

        if municipio_a_buscar:
            hospitais = hospitais.filter(municipio__iexact=municipio_a_buscar)

    if "categoria" in request.GET:
        categoria_a_buscar = request.GET['categoria']

        if categoria_a_buscar:
            hospitais = hospitais.filter(categoria__iexact=categoria_a_buscar)

    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']

        if nome_a_buscar:
            hospitais = hospitais.filter(nome__icontains=nome_a_buscar)

    context = {"hospitais": hospitais, "buscar": buscar2, "filter":filter_form}

    return render(request, "medconnect/locaisdeatendimento.html", context)

def mais_informacoes(request, hospital_cnes):
    hospital = get_object_or_404(Hospital, pk=hospital_cnes)
    buscar2 = BuscarForms()
    filter_form = FilterForms()
    counter = (1, 2, 3, 4, 5)
    context = {"hospital": hospital, "buscar": buscar2, "filter":filter_form, "counter":counter}

    return render(request, "medconnect/maisinformacoes.html", context)

def avaliar_hospital(request, hospital_cnes):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário precisa estar autenticado para avaliar hospitais")
        return redirect('mais_informacoes', hospital_cnes)

    hospital = get_object_or_404(Hospital, pk=hospital_cnes)
    buscar2 = BuscarForms()
    filter_form = FilterForms()
    context = {"hospital": hospital, "buscar": buscar2, "filter":filter_form}

    if request.method == "POST":
        numero = Avaliacao.objects.filter(usuario=request.user.username).count() + 1
        risco = request.POST["risco"]
        horario_entrada = datetime.strptime(request.POST["horario_entrada"],"%Y-%m-%dT%H:%M")
        horario_atendimento = datetime.strptime(request.POST["horario_atendimento"],"%Y-%m-%dT%H:%M")
        horario_saida = datetime.strptime(request.POST["horario_saida"],"%Y-%m-%dT%H:%M")
        duracao = horario_atendimento - horario_entrada
        avaliacao = request.POST["avaliacao"]
        observacao = request.POST["observacao"]

        Avaliacao.objects.create(
            numero=numero,
            usuario=request.user.username,
            hospital=hospital,
            risco=risco,
            horario_entrada=horario_entrada,
            horario_atendimento=horario_atendimento,
            horario_saida=horario_saida,
            duracao=duracao,
            avaliacao=avaliacao,
            observacao=observacao
        )

        return redirect('mais_informacoes', hospital_cnes)

    return render(request, "medconnect/avaliarhospital.html", context)

def duvidas_frequentes(request):
    buscar2 = BuscarForms()
    filter_form = FilterForms()
    context = {"buscar": buscar2, "filter":filter_form}

    return render(request, 'medconnect/duvidas_frequentes.html', context)

def sobre_nos(request):
    buscar2 = BuscarForms()
    filter_form = FilterForms()
    context = {"buscar": buscar2, "filter":filter_form}

    return render(request, 'medconnect/SobreNos.html', context)

def cadastro(request):
    if request.method == "POST":

        email = request.POST["email"]
        senha_1 = request.POST["senha_1"]
        senha_2 = request.POST["senha_2"]
        nome = request.POST["nome"]
        sobrenome = request.POST["sobrenome"]
        data_nascimento = datetime.strptime(request.POST["data_nascimento"],"%Y-%m-%d")
        genero = request.POST["genero"]

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email já cadastrado")
            return redirect('cadastro')
        
        if senha_1 != senha_2:
            messages.error(request, "Digite senhas iguais para concluir o cadastro")
            return redirect('cadastro')

        usuario = User.objects.create_user(
            username=email,
            email=email,
            password=senha_1,
            first_name=nome,
            last_name=sobrenome
        )

        usuario.save()

        Dados.objects.create(usuario=usuario, data_nascimento=data_nascimento, genero=genero)

        login(request, usuario)
        messages.success(request, "Usuário cadastrado com sucesso!")
        return redirect('index')

    context = {"cadastro":cadastro}

    return render(request, 'medconnect/criar_conta_2.html', context)

def login_site(request):
    if request.method == "POST":
        usuario = request.POST["usuario"]
        senha = request.POST["senha"]

        user = authenticate(request, username=usuario, password=senha)

        if user is not None:
            login(request, user)
            messages.success(request, f"{usuario} autenticado com sucesso!")
            return redirect("index")

        else:
            messages.error(request, "Email ou senha incorretos", extra_tags="login")
            return redirect("index")

def confirma_email(request):
    if request.method == "POST":
        email = request.POST["email"]

        if User.objects.filter(email__exact=email).exists():

            gerador = PasswordResetTokenGenerator()
            usuario = User.objects.get(email=email)
            token = gerador.make_token(usuario)
            username = usuario.username
            context = {"token":token, "username": username}
            # print(gerador.check_token(usuario, token))

            send_mail(
                "Redefinição de Senha",
                message=
                "Uma requisição de redefinição de senha foi feita no site MedConnect para a conta vinculada a este email, "
                f"para prosseguir com a redefinição basta acessar o seguinte link: http://{request.get_host()}/redefinir_senha/{username}/{token}. "
                "Caso a requisição não tenha sido feita por você por favor ignore este email.",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email,],
            )
            messages.success(request, "Email de redefinição de senha enviado com sucesso!")
        else:
            messages.error(request, "Nenhum usuário encontrado com o email informado")

    return redirect("index")

def logout_site(request):
    logout(request)
    messages.success(request, "Logout efetuado com sucesso!")
    return redirect('index')

def redefinir_senha(request, username, token):
    usuario = User.objects.get(username=username)

    if request.method == "POST":
        if request.POST["senha_1"] != request.POST["senha_2"]:
            return redirect("redefinir_senha", username, token)

        senha = request.POST["senha_1"]
        usuario.set_password(senha)
        usuario.save(force_update=True)

        messages.success(request, "Senha redefinida com sucesso!")
        return redirect("index")

    gerador = PasswordResetTokenGenerator()

    if gerador.check_token(usuario, token):

        context = {"username":username, "token":token}

        return render(request,'medconnect/RedefinirSenha.html', context)

def minhas_avaliacoes(request):
    if not request.user.is_authenticated:
        messages.error(request, "Realize login para visualizar suas avaliações")
        return redirect("index")

    buscar2 = BuscarForms()
    filter_form = FilterForms()
    counter = (1, 2, 3, 4, 5)
    avaliacoes = Avaliacao.objects.filter(usuario__exact=request.user.username).order_by("numero")
    context = {"buscar": buscar2, "filter":filter_form, "counter":counter, "avaliacoes":avaliacoes}

    return render(request, "medconnect/minhasavaliacoes.html", context)

def pesquisar_avaliacoes(request):
    if not request.user.is_authenticated:
        messages.error(request, "Realize login para visualizar suas avaliações")
        return redirect("index")

    buscar2 = BuscarForms()
    filter_form = FilterForms()
    counter = (1, 2, 3, 4, 5)
    avaliacoes = Avaliacao.objects.filter(usuario__exact=request.user.username).order_by("numero")
    if "hospital" in request.GET:
        avaliacoes = Avaliacao.objects.filter(usuario__exact=request.user.username).filter(hospital__nome__icontains=request.GET["hospital"]).order_by("numero")
    context = {"buscar": buscar2, "filter":filter_form, "counter":counter, "avaliacoes":avaliacoes}

    return render(request, "medconnect/minhasavaliacoes.html", context)

def avaliacao_completa(request, avaliacao_id):
    if not request.user.is_authenticated:
        messages.error(request, "Realize login para visualizar suas avaliações")
        return redirect("index")

    buscar2 = BuscarForms()
    filter_form = FilterForms()
    counter = (1, 2, 3, 4, 5)
    avaliacao = get_object_or_404(Avaliacao, pk=avaliacao_id)
    context = {"buscar": buscar2, "filter":filter_form, "counter":counter, "avaliacao":avaliacao}

    return render(request, "medconnect/av_completa.html", context)

def triagem(request):
    filter_form = FilterForms()
    context = {"filter":filter_form}

    if request.method=="POST":
        if "idade" not in request.POST or "termo" not in request.POST:
            messages.error(request,"Você precisa selecionar os campos.")
            return redirect("triagem")
        elif request.POST["idade"] == "1":
            return redirect("crianca1")
        else:
            return redirect("adulto1")
    return render(request, 'medconnect/PreTriagem.html', context)

def adulto1(request):
    filter_form = FilterForms()
    context = {"filter":filter_form}

    if request.method=="POST":
        if "quest_a1" not in request.POST:
            return redirect("adulto2")   
        if request.POST["quest_a1"] == "1":
            return redirect("resultado_vermelho")
    return render(request, 'medconnect/adulto1.html', context)

def crianca1(request):
    filter_form = FilterForms()
    context = {"filter":filter_form}

    if request.method=="POST":
        if "quest_b1" not in request.POST:
            return redirect("crianca2")   
        if request.POST["quest_b1"] == "1":
            return redirect("resultado_vermelho")
    return render(request, 'medconnect/criança1.html' )

def resultado_vermelho(request):
    filter_form = FilterForms()
    context = {"filter":filter_form}
    
    return render(request, 'medconnect/vermelho_triagem.html', context)

def crianca2(request):
    filter_form = FilterForms()
    context = {"filter":filter_form}

    if request.method=="POST":
        if "quest_b2" not in request.POST:
            return redirect("crianca3")   
        if request.POST["quest_b2"] == "1":
            return redirect("resultado_laranja")
    return render(request, 'medconnect/criança2.html', context) 

def adulto2(request):
    filter_form = FilterForms()
    context = {"filter":filter_form}

    if request.method=="POST":
        if "quest_a2" not in request.POST:
            return redirect("adulto3")   
        if request.POST["quest_a2"] == "1":
            return redirect("resultado_laranja")
    return render(request, 'medconnect/adulto2.html', context)

def resultado_laranja(request):
    filter_form = FilterForms()
    context = {"filter":filter_form}

    return render(request, 'medconnect/laranja_triagem.html', context)

def crianca3(request):
    filter_form = FilterForms()
    context = {"filter":filter_form}

    if request.method=="POST":
        if "quest_b3" not in request.POST:
            return redirect("crianca4")   
        if request.POST["quest_b3"] == "1":
            return redirect("resultado_amarelo")
    return render(request, 'medconnect/criança3.html', context)

def adulto3(request):
    filter_form = FilterForms()
    context = {"filter":filter_form}

    if request.method=="POST":
        if "quest_a3" not in request.POST:
            return redirect("adulto4")   
        if request.POST["quest_a3"] == "1":
            return redirect("resultado_amarelo")
    return render(request, 'medconnect/adulto3.html', context)

def resultado_amarelo(request):
    filter_form = FilterForms()
    context = {"filter":filter_form}

    return render(request, 'medconnect/amarelo_triagem.html', context)

def crianca4(request):
    filter_form = FilterForms()
    context = {"filter":filter_form}

    if request.method=="POST":
        if "quest_b4" not in request.POST:
            return redirect("resultado_azul")   
        if request.POST["quest_b4"] == "1":
            return redirect("resultado_verde")
    return render(request,'medconnect/criança4.html', context)

def adulto4(request):
    filter_form = FilterForms()
    context = {"filter":filter_form}

    if request.method=="POST":
        if "quest_a4" not in request.POST:
            return redirect("resultado_azul")   
        if request.POST["quest_a4"] == "1":
            return redirect("resultado_verde")
    return render(request, 'medconnect/adulto4.html', context)

def resultado_azul(request):
    filter_form = FilterForms()
    context = {"filter":filter_form}

    return render(request, 'medconnect/azul_triagem.html', context)

def resultado_verde(request):
    filter_form = FilterForms()
    context = {"filter":filter_form}

    return render(request, 'medconnect/verde_triagem.html', context)

def meus_dados(request):
    if not request.user.is_authenticated:
        messages.error(request, "Realize login para visualizar seus dados")
        return redirect("index")

    buscar2 = BuscarForms()
    filter_form = FilterForms()
    context = {"buscar": buscar2, "filter":filter_form}

    return render(request, "medconnect/meusdados.html", context)

def editar_dados(request):
    if not request.user.is_authenticated:
        messages.error(request, "Realize login para visualizar seus dados")
        return redirect("index")

    if request.method == "POST":
        dados = json.loads(request.POST["dados"])
        dados.pop("dados")
        novos_dados = Dados.objects.get(usuario=request.user)
        user = request.user

        if dados["p_nome"] != "":
            user.first_name = dados["p_nome"]

        if dados["s_nome"] != "":
            user.last_name = dados["s_nome"]

        if dados["data_nascimento"] != "":
            novos_dados.data_nascimento = datetime.strptime(request.POST["data_nascimento"],"%Y-%m-%d")
        
        if "genero" in dados:
            novos_dados.genero = dados["genero"]

        if dados["profissao"] != "":
            novos_dados.profissao = dados["profissao"]
        
        if dados["endereco"] != "":
            novos_dados.endereco = dados["endereco"]

        if dados["telefone"] != "":
            novos_dados.telefone = dados["telefone"]

        if dados["peso"] != "":
            novos_dados.peso = dados["peso"]

        if dados["altura"] != "":
            novos_dados.altura = dados["altura"]

        if dados["tipo_sanguineo"] != "":
            novos_dados.tipo_sanguineo = dados["tipo_sanguineo"]

        if "sim-nao1" in dados:
            if dados["sim-nao1"] == "nao":
                novos_dados.fumo_alcool = "n"

            if dados["sim-nao1"] != "nao" and "freq1" in dados:
                novos_dados.fumo_alcool = dados["freq1"]

        if "sim-nao2" in dados:
            if dados["sim-nao1"] == "nao":
                novos_dados.exercicio_frequencia = "n"

            if dados["sim-nao2"] != "nao" and "freq2" in dados:
                if dados["exercicio"] != "":
                    novos_dados.exercicio = dados["exercicio"]
                    novos_dados.exercicio_frequencia = dados["freq2"]

        if "sim-nao3" in dados:
            Doencas.objects.filter(user=request.user).delete()

            if dados["sim-nao3"] != "nao":
                if "doenca_cronica" in dados:
                    doencas = dados["doenca_cronica"]

                    if isinstance(doencas, str):
                        if doencas != "":
                            Doencas.objects.create(user=request.user, doenca=doencas)

                    if isinstance(doencas, list):
                        for doenca in doencas:
                            if doenca != "":
                                Doencas.objects.create(user=request.user, doenca=doenca)

        if "sim-nao4" in dados:
            Sintomas.objects.filter(user=request.user).delete()

            if dados["sim-nao4"] != "nao":
                sintomas = dados["sintomas"]

                if isinstance(sintomas, str):
                    if sintomas != "":
                        Sintomas.objects.create(user=request.user, sintoma=sintomas)

                if isinstance(sintomas,list):
                    for sintoma in sintomas:
                        if sintoma != "":
                            Sintomas.objects.create(user=request.user, sintoma=sintoma)

        if "sim-nao5" in dados:
            Diagnostico.objects.filter(user=request.user).delete()

            if dados["sim-nao5"] != "nao":
                diagnosticos = dados["doencas-diag"]

                if isinstance(diagnosticos, str):
                    if diagnosticos != "":
                        Diagnostico.objects.create(user=request.user, diagnostico=diagnosticos)

                if isinstance(diagnosticos, list):
                    for diagnostico in diagnosticos:
                        if diagnostico != "":
                            Diagnostico.objects.create(user=request.user, diagnostico=diagnostico)

        if "sim-nao6" in dados:
            Cirurgia.objects.filter(user=request.user).delete()

            if dados["sim-nao6"] != "nao":
                cirurgias = dados["cirurgias"]
                data_cirurgia = dados["data_cirurgia"]

                if isinstance(cirurgias, str) and isinstance(data_cirurgia, str):
                    if cirurgias != "" and data_cirurgia != "":
                        data = datetime.strptime(data_cirurgia,"%Y-%m-%d")
                        Cirurgia.objects.create(user=request.user, cirurgia=cirurgias, data=data)

                if isinstance(cirurgias, list) and isinstance(data_cirurgia, list):
                    for i in range(len(cirurgias)):
                        if cirurgias[i] != "" and data_cirurgia[i] != "":
                            data = datetime.strptime(data_cirurgia[i],"%Y-%m-%d")
                            Cirurgia.objects.create(user=request.user, cirurgia=cirurgias[i], data=data)

        if "sim-nao7" in dados:
            Internacao.objects.filter(user=request.user).delete()

            if dados["sim-nao7"] != "nao":
                motivo = dados["motivo_internacao"]
                tempo_internacao = dados["tempo_internacao"]
                data_internacao = dados["data_internacao"]

                if isinstance(motivo, str) and isinstance(tempo_internacao, str) and isinstance(data_internacao, str):
                    if motivo != "" and tempo_internacao != "" and data_internacao != "":
                        data = datetime.strptime(data_internacao,"%Y-%m-%d")
                        Internacao.objects.create(user=request.user, tempo=tempo_internacao, data=data, internacao=motivo)

                if isinstance(motivo, list) and isinstance(tempo_internacao, list) and isinstance(data_internacao, list):
                    for i in range(len(motivo)):
                        if motivo[i] != "" and tempo_internacao[i] != "" and data_internacao[i] != "":
                            data = datetime.strptime(data_internacao[i],"%Y-%m-%d")
                            Internacao.objects.create(user=request.user, tempo=tempo_internacao[i], data=data, internacao=motivo[i])

        if "sim-nao8" in dados:
            Condicao_familiar.objects.filter(user=request.user).delete()

            if dados["sim-nao8"] != "nao":
                if "condicao" in dados and "grau_parentesco" in dados:
                    grau_parentesco = dados["grau_parentesco"]
                    condicao = dados["condicao"]

                    if isinstance(grau_parentesco, str) and isinstance(condicao, str):
                        if grau_parentesco != "" and condicao != "":
                            Condicao_familiar.objects.create(user=request.user, condicao=condicao, grau_parentesco=grau_parentesco)

                    if isinstance(grau_parentesco, list) and isinstance(condicao, list):
                        for i in range(len(condicao)):
                            if grau_parentesco[i] != "" and condicao[i] != "":
                                Condicao_familiar.objects.create(user=request.user, condicao=condicao[i], grau_parentesco=grau_parentesco[i])

        if "sim-nao9" in dados:
            Medicamento.objects.filter(user=request.user).filter(tipo__iexact="1").delete()

            if dados["sim-nao9"] != "nao":
                if "medicamento_cp" in dados and "freq_med_cp" in dados and "freq3" in dados: 
                    medicamento_cp = dados["medicamento_cp"]
                    freq_cp = dados["freq_med_cp"]
                    freq3 = dados["freq3"]

                    if isinstance(medicamento_cp, str) and isinstance(freq_cp, str) and isinstance(freq3, str):
                        if medicamento_cp != "" and freq_cp != "" and freq3 != "":
                            Medicamento.objects.create(user=request.user, 
                                tipo="1", 
                                medicamento=medicamento_cp, 
                                frequencia=freq3,
                                numero_frequencia=freq_cp)

                    if isinstance(medicamento_cp, list) and isinstance(freq_cp, list) and isinstance(freq3, list):
                        for i in range(len(medicamento_cp)):
                            if medicamento_cp[i] != "" and freq_cp[i] != "" and freq3[i] != "":
                                Medicamento.objects.create(user=request.user, 
                                    tipo="1", 
                                    medicamento=medicamento_cp[i], 
                                    frequencia=freq3[i],
                                    numero_frequencia=freq_cp[i])

        if "sim-nao10" in dados:
            Medicamento.objects.filter(user=request.user).filter(tipo__iexact="2").delete()

            if dados["sim-nao10"] != "nao":
                if "medicamento_sp" in dados and "freq_med_sp" in dados and "freq4" in dados:
                    medicamento_sp = dados["medicamento_sp"]
                    freq_sp = dados["freq_med_sp"]
                    freq4 = dados["freq4"]

                    if isinstance(medicamento_sp, str) and isinstance(freq_sp, str) and isinstance(freq4, str):
                        if medicamento_sp != "" and freq_sp != "" and freq4 != "":
                            Medicamento.objects.create(user=request.user, 
                                tipo="2", 
                                medicamento=medicamento_sp, 
                                frequencia=freq4,
                                numero_frequencia=freq_sp)

                    if isinstance(medicamento_sp, list) and isinstance(freq_sp, list) and isinstance(freq4, list):
                        for i in range(len(medicamento_sp)):
                            if medicamento_sp[i] != "" and freq_sp[i] != "" and freq4[i] != "":
                                Medicamento.objects.create(user=request.user, 
                                    tipo="2", 
                                    medicamento=medicamento_sp[i], 
                                    frequencia=freq4[i],
                                    numero_frequencia=freq_sp[i])

        novos_dados.save()
        user.save()
        messages.success(request, "Dados alterados com sucesso!")
        return redirect("meus_dados")

    buscar2 = BuscarForms()
    filter_form = FilterForms()
    context = {"buscar": buscar2, "filter":filter_form}

    return render(request, "medconnect/editardados.html", context)

from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.db.models import Avg
from django.contrib.auth.models import User
from django.utils import timezone
from .models import *
from datetime import timedelta

@receiver(post_save, sender=Avaliacao)
def update_time(sender, instance, created, **kwargs):
    if created:
        hospital = instance.hospital
        risco = instance.risco
        duracao = Avaliacao.objects.filter(hospital=hospital).filter(risco=risco).aggregate(Avg("duracao", default=timedelta(minutes=0)))
        minutos = round(duracao["duracao__avg"].seconds / 60)

        avaliacao = Avaliacao.objects.filter(hospital=hospital).aggregate(Avg("avaliacao", default=0))
        nota = avaliacao["avaliacao__avg"]
        hospital.nota = nota

        if risco == "EMERGENTE":
            hospital.tempo_emergente = minutos

        if risco == "MUITO_URGENTE":
            hospital.tempo_muito_urgente = minutos

        if risco == "URGENTE":
            hospital.tempo_urgente = minutos

        if risco == "POUCO_URGENTE":
            hospital.tempo_pouco_urgente = minutos

        if risco == "NAO_URGENTE":
            hospital.tempo_nao_urgente = minutos

        hospital.atualizacao = timezone.now()
        hospital.save()
from django.db import models

class Contato(models.Model):
    nome = models.CharField(max_length=50, verbose_name='Nome')
    email = models.EmailField(verbose_name='E-mail')
    mensagem = models.TextField(verbose_name='Mensagem')
    data = models.DateTimeField(verbose_name='Enviado em', auto_now_add=True)

class Reserva(models.Model):
    nomeDoPet = models.CharField(max_length=50, verbose_name='Nome do PET')
    raca = models.CharField(max_length=40, verbose_name='Raça')
    nomeDoTutor = models.CharField(max_length=80, verbose_name='Nome do TUTOR')
    telefone = models.CharField(max_length=11, verbose_name='Telefone')
    dia = models.DateTimeField(verbose_name='Dia')
    observacoes = models.TextField(verbose_name='Observações')

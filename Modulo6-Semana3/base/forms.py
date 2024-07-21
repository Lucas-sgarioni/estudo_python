from django import forms
from base.models import Contato, Reserva
import datetime

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'mensagem']

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['nomeDoPet', 'raca', 'nomeDoTutor', 'telefone', 'dia', 'observacoes']
        widgets = {
            'dia': forms.DateInput(attrs={'type':'date','min': str(datetime.date.today())}),
        }

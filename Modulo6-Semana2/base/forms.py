from django import forms

class ContatoForm(forms.Form):
    nome = forms.CharField()
    email = forms.EmailField()
    mensagem = forms.CharField(widget=forms.Textarea)

class ReservaForm(forms.Form):
    nomeDoPet = forms.CharField(label="Nome do PET")
    raca = forms.CharField(label="Raça")
    nomeDoTutor = forms.CharField(label="Nome do tutor")
    telefone = forms.CharField(max_length=11)
    dia = forms.DateField(label="Data da reserva", widget=forms.widgets.DateInput(attrs={"type": "date"}))
    observacoes = forms.CharField(widget=forms.Textarea, label="Observações")
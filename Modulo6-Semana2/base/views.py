from django.shortcuts import render
from base.forms import ContatoForm, ReservaForm

# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')

def contato(request):
    sucesso = False

    if request.method == 'GET':
        form = ContatoForm()
    elif request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            sucesso = True

    context = {
        'formulario': form,
        'sucesso': sucesso
    }
    return render(request, 'contato.html', context)

def reserva(request):
    sucesso = False

    if request.method == 'GET':
        form = ReservaForm()
    elif request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            sucesso = True
# views.py

    context = {
        'formulario': form,
        'sucesso': sucesso,
    }

    return render(request, 'reserva.html', context)

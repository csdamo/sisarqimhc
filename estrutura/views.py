from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import ProtectedError
from .models import Estrutura
from .forms import EstruturaForm


def cria_nivel_estrutura(estrutura):
    nivel = 0
    estrutura_nivel_superior = estrutura.estrutura_nivel_superior
    
    if estrutura_nivel_superior:
        nivel = int(estrutura_nivel_superior.nivel)
        
    estrutura.nivel = nivel + 1
    
    
@login_required
def lista(request):
    lista = Estrutura.objects.all().order_by('nivel')
    context = {'lista': lista}
    return render(request, 'estrutura/lista.html', context=context)

@login_required
def detalhe(request, id):
    estrutura = get_object_or_404(Estrutura, pk=id)
    context = {'dados': estrutura}
    return render(request, 'estrutura/detalhe.html', context=context)

@login_required
def novo(request):
    form = EstruturaForm()
    
    if request.method == 'POST':
        form = EstruturaForm(request.POST)
       
        if form.is_valid():
            estrutura = form.save(commit=False)
            cria_nivel_estrutura(estrutura)
            estrutura.save()
            messages.info(request, 'Novo registro criado com sucesso.')
            return redirect('/estrutura/lista') 
                
    context = {
        'form': form,
        'acao': 'Novo',
        'titulo': 'Estrutura',
    }
    return render(request, 'estrutura/formulario.html', context=context)

@login_required
def edita(request, id):
    
    estrutura = get_object_or_404(Estrutura, pk=id)
    estrutura_nivel_superior = estrutura.estrutura_nivel_superior
    nivel_estrutura_superior_anterior = None
    if estrutura_nivel_superior:
        nivel_estrutura_superior_anterior = estrutura_nivel_superior.nivel
    form = EstruturaForm(instance=estrutura)
    
    if request.method == 'POST':
        form = EstruturaForm(request.POST, instance=estrutura)
       
        if form.is_valid():
            estrutura = form.save(commit=False)
            nivel_estrutura_superior_atual = estrutura.estrutura_nivel_superior.nivel   
            
            if nivel_estrutura_superior_anterior != nivel_estrutura_superior_atual:
                cria_nivel_estrutura(estrutura)
            estrutura.save()
            messages.info(request, 'Registro editado com sucesso.')
            return redirect('/estrutura/lista') 
        
    context = {
        'form': form,
        'acao': 'Edita',
        'titulo': 'Estrutura',
    }
    return render(request, 'estrutura/formulario.html', context=context)

@login_required
def deleta(request, id):
    estrutura = get_object_or_404(Estrutura, pk=id)
    try:
        # estrutura.delete()
        messages.info(request, 'Registro deletado com sucesso.')
        return redirect('/estrutura/lista')
    except ProtectedError:
        messages.warning(request, 'Registro não pode ser deletado')
        return redirect('/estrutura/list')
    
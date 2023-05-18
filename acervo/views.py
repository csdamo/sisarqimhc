from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import ProtectedError
from .models import Acervo
from .forms import AcervoForm

@login_required
def lista(request):
    lista = Acervo.objects.all().order_by('ordem_exibicao')
    context = {'lista': lista}
    return render(request, 'acervo/lista.html', context=context)

@login_required
def detalhe(request, id):
    acervo = get_object_or_404(Acervo, pk=id)
    context = {'dados': acervo}
    return render(request, 'acervo/detalhe.html', context=context)

@login_required
def novo(request):
    form = AcervoForm()
    
    if request.method == 'POST':
        form = AcervoForm(request.POST)
       
        if form.is_valid():
            acervo = form.save(commit=False)
            acervo.save()
            messages.info(request, 'Novo registro criado com sucesso.')
            return redirect('/acervo/lista')  
                
    context = {
        'form': form,
        'acao': 'Novo',
        'titulo': 'Acervo',
    }
    return render(request, 'acervo/formulario.html', context=context)

@login_required
def edita(request, id):
    
    acervo = get_object_or_404(Acervo, pk=id)
    form = AcervoForm(instance=acervo)
    
    if request.method == 'POST':
        form = AcervoForm(request.POST, instance=acervo)
       
        if form.is_valid():
            acervo = form.save(commit=False)
            acervo.save()
            messages.info(request, 'Registro editado com sucesso.')
            return redirect('/acervo/lista') 
                
    context = {
        'form': form,
        'acao': 'Edita',
        'titulo': 'Acervo',
    }
    return render(request, 'acervo/formulario.html', context=context)

@login_required
def deleta(request, id):
    acervo = get_object_or_404(Acervo, pk=id)
    try:
        acervo.delete()
        messages.info(request, 'Registro deletado com sucesso.')
        return redirect('/acervo/lista')
    except ProtectedError:
        messages.warning(request, 'Registro não pode ser deletado')
        return redirect('/acervo/list')

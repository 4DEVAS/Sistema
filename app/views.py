from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from app.forms import EmpresaForm
from app.models import Empresa
from app.forms import ProdutoForm
from app.models import Produto
from django.core.paginator import Paginator

# Criando as partes da empresa.
def home(request):
    data = {}
    search = request.GET.get('search')
    search_produtos = request.GET.get('search_produtos')
    if search:
        data['empresas'] = Empresa.objects.filter(nome__icontains=search)
        data['db'] = Produto.objects.all()
    elif search_produtos:
        data['empresas'] = Empresa.objects.all()
        data['db'] = Produto.objects.filter(nome__icontains=search_produtos)
    else:
        data['empresas'] = Empresa.objects.all()
        data['db'] = Produto.objects.all()
    return render(request, 'home.html', data)


def index(request):
    return render(request, 'index.html')

def form(request):
    data = {}
    data['form'] = EmpresaForm()
    return render(request, 'form.html', data)


def home_produto(request):
    data = {}

    #data['db'] = Produto.objects.get(pk=pk)

    search = request.GET.get('search')
    search_produtos = request.GET.get('search_produtos')

    if search:
        data['empresas'] = Empresa.objects.filter(nome__icontains=search)
        data['db'] = Produto.objects.all()
    else:
        data['empresas'] = Empresa.objects.all()
        data['db'] = Produto.objects.all()
        #data['empresas'] = Empresa.objects.all()
        #data['db'] = Produto.objects.get(pk=pk)


    return render(request, 'home_produto.html', data)


def produto_novo(request):
    data = {}
    data['form1'] = ProdutoForm()
    data['empresas'] = Empresa.objects.all()
    return render(request, 'produto_novo.html', data)

def create(request):
    print(request.POST)
    form = EmpresaForm(request.POST or None)
    if form.is_valid():
        print("Valido")
        form.save()
        return HttpResponseRedirect('/home')
    else:
        print("Teste")
        return HttpResponseRedirect('/home')




def view(request, pk):
    data = {}
    data['db'] = Empresa.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Empresa.objects.get(pk=pk)
    data['form'] = EmpresaForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['db'] = Empresa.objects.get(pk=pk)
    form = EmpresaForm(request.POST or None, instance=data['db'])
    print(form)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/home')

def delete(request, pk):
    db = Empresa.objects.get(pk=pk)
    db.delete()
    #return redirect('home')
    return HttpResponseRedirect('/home')

# Criando as partes da produto.
def form1(request):
    data = {}
    data['form1'] = ProdutoForm()
    return render(request, 'produto_novo.html', data)

def produto_create(request):
    print(request.POST)
    form = ProdutoForm(request.POST or None)
    if form.is_valid():
        print("Valido")
      #  a = request.POST['emp']
       # print (a)
        form.save()
        return HttpResponseRedirect('/home_produto')
    else:
        print("Teste")
        return HttpResponseRedirect('/home_produto')

def produto_view(request, pk):
    data = {}
    data['db'] = Produto.objects.get(pk=pk)
    return render(request, 'view_prod.html', data)

def produto_edit(request, pk):
    data = {}
    data['db'] = Produto.objects.get(pk=pk)
    data['form1'] = ProdutoForm(instance=data['db'])
    return render(request, 'produto_edit.html', data)

def produto_update(request, pk):
    data = {}
    data['db'] = Produto.objects.get(pk=pk)

    form1 = ProdutoForm(request.POST or None, instance=data['db'])
    print(form1)
    if form1.is_valid():
        form1.save()
        print("Passou aqui")

        return HttpResponseRedirect('/home_produto')
    else:
        print("Teste")
        return HttpResponseRedirect('/home_produto')

def produto_delete(request, pk):
    db = Produto.objects.get(pk=pk)
    db.delete()
    return HttpResponseRedirect('/home_produto')



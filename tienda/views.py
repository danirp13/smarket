from django.shortcuts import render
from django.http import HttpResponse
from tienda.models import Categoria, Producto
from django.views.generic import ListView, DetailView
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import UpdateView, CreateView, DeleteView

# Create your views here.

def base(request):
	return render(request, 'base.html')

#------------------------------------producto------------------------------------

class ProductoListView(ListView):
	model = Producto

class ProductoDetailView(DetailView):
	model = Producto	



#----------------------------------categoria-------------------------------------

class CategoriaListView(ListView):
	model = Categoria


class CategoriaDetailView(DetailView):
	model = Categoria


class CategoriaUpdate(UpdateView):
	model=Categoria
	fields='__all__'

class CategoriaDelete(DeleteView):
	model=Categoria
	success_url=reverse_lazy('categoria-list')

class CategoriaCreate(CreateView):
	model=Categoria
	fields='__all__'






def categoria(request):
	categoria_list = Categoria.objects.all()
	context = {'object_list': categoria_list}
	return render(request, 'tienda/categoria.html', context)


def categoria_detail(request, categoria_id):
	categoria = Categoria.objects.get(id_categoria=categoria_id)
	context = {'object': categoria}
	return render(request, 'tienda/categoria_detail.html', context)	
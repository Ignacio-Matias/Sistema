from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView

from  apps.catalogos.forms import *
from apps.catalogos.models import *

# cat_tipo
def catalogo_view(request):
	if request.method == 'POST':
		form = Cat_Tipo_Form(request.POST)
		if form.is_valid():
			form.save()
		return redirect('catalogos:catalogo_listar')
	else:
		form = Cat_Tipo_Form()
		return render(request, 'catalogos/catalogo_form.html', {'form':form})

class catalogo_list(ListView):
	model = cat_tipo
	template_name = 'catalogos/catalogo_list.html'
	paginate_by = 4

class catalogo_update(UpdateView):
	model = cat_tipo
	form_class = Cat_Tipo_Form
	template_name = 'catalogos/catalogo_form.html'
	success_url = reverse_lazy('catalogos:catalogo_listar')

class catalogo_delete(DeleteView):
	model = cat_tipo
	template_name = 'catalogos/catalogo_delete.html'
	success_url = reverse_lazy('catalogos:catalogo_listar')

# cat_tecnologias
def tecnologia_list(request):
	tecnologia = cat_tecnologias.objects.all().order_by('id')
	contexto = {'tecnologias':tecnologia}
	return render(request, 'catalogos/Tecnologias/tecnologias_list.html', contexto)

def tecnologia_view(request):
	if request.method == 'POST':
		form = Cat_Tecnologias_Form(request.POST)
		if form.is_valid():
			form.save()
		return redirect('catalogos:tecnologia_listar')
	else:
		form = Cat_Tecnologias_Form()
		return render(request, 'catalogos/Tecnologias/tecnologias_form.html', {'form':form})

class tecnologia_update(UpdateView):
	model = cat_tecnologias
	form_class = Cat_Tecnologias_Form
	template_name = 'catalogos/Tecnologias/tecnologias_form.html'
	success_url = reverse_lazy('catalogos:tecnologia_listar')
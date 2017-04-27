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

class tecnologia_delete(DeleteView):
	model = cat_tecnologias
	template_name = 'catalogos/Tecnologias/tecnologias_delete.html'
	success_url = reverse_lazy('catalogos:tecnologia_listar')

# cat_personas
def persona_list(request):
	persona = cat_personas.objects.all().order_by('id')
	contexto = {'personas':persona}
	return render(request, 'catalogos/Personas/personas_list.html', contexto)

def persona_view(request):
	if request.method == 'POST':
		form = Cat_personas_Form(request.POST)
		if form.is_valid():
			form.save()
		return redirect('catalogos:persona_listar')
	else:
		form = Cat_personas_Form()
		return render(request, 'catalogos/Personas/personas_form.html', {'form':form})

class persona_update(UpdateView):
	model = cat_personas
	form_class = Cat_personas_Form
	template_name = 'catalogos/Personas/personas_form.html'
	success_url = reverse_lazy('catalogos:persona_listar')

class persona_delete(DeleteView):
	model = cat_personas
	template_name = 'catalogos/Personas/personas_delete.html'
	success_url = reverse_lazy('catalogos:persona_listar')

# cat_especialidad
def especialidad_list(request):
	especialidad = cat_especialidad.objects.all().order_by('id')
	contexto = {'especialidades':especialidad}
	return render(request, 'catalogos/Especialidades/especialidad_list.html', contexto)

def especialidad_view(request):
	if request.method == 'POST':
		form = Cat_Especialidad_Form(request.POST)
		if form.is_valid():
			form.save()
		return redirect('catalogos:especialidad_listar')
	else:
		form = Cat_Especialidad_Form()
		return render(request, 'catalogos/Especialidades/especialidad_form.html', {'form':form})

class especialidad_update(UpdateView):
	model = cat_especialidad
	form_class = Cat_Especialidad_Form
	template_name = 'catalogos/Especialidades/especialidad_form.html'
	success_url = reverse_lazy('catalogos:especialidad_listar')

class especialidad_delete(DeleteView):
	model = cat_especialidad
	template_name = 'catalogos/Especialidades/especialidad_delete.html'
	success_url = reverse_lazy('catalogos:especialidad_listar')

# cat_estatus
def estatus_list(request):
	estatus = cat_estatus.objects.all().order_by('id')
	contexto = {'estatus':estatus}
	return render(request, 'catalogos/Estatus/estatus_list.html', contexto)

def estatus_view(request):
	if request.method == 'POST':
		form = Cat_Estatus_Form(request.POST)
		if form.is_valid():
			form.save()
		return redirect('catalogos:estatus_listar')
	else:
		form = Cat_Estatus_Form()
		return render(request, 'catalogos/Estatus/estatus_form.html', {'form':form})

class estatus_update(UpdateView):
	model = cat_estatus
	form_class = Cat_Estatus_Form
	template_name = 'catalogos/Estatus/estatus_form.html'
	success_url = reverse_lazy('catalogos:estatus_listar')

class estatus_delete(DeleteView):
	model = cat_estatus
	template_name = 'catalogos/Estatus/estatus_delete.html'
	success_url = reverse_lazy('catalogos:estatus_listar')

# cat_documentos
def documentos_list(request):
	documento = cat_documentos.objects.all().order_by('id')
	contexto = {'documentos':documento}
	return render(request, 'catalogos/Documentos/documentos_list.html', contexto)

def documentos_view(request):
	if request.method == 'POST':
		form = Cat_Documentos_Form(request.POST or None, request.FILES or None)
		if form.is_valid():
			form.save()
		return redirect('catalogos:documentos_listar')
	else:
		form = Cat_Documentos_Form()
		return render(request, 'catalogos/Documentos/documentos_form.html', {'form':form})

def documentos_update(request, id):
    documento = cat_documentos.objects.get(id=id)
    if request.method == 'GET':
        form = Cat_Documentos_Form(instance=documento)
    else:
        form = Cat_Documentos_Form(request.POST or None, request.FILES or None, instance=documento)
        if form.is_valid():
            form.save()
        return redirect('catalogos:documentos_listar')
    return render(request, 'catalogos/Documentos/documentos_form.html', {'form': form})

class documentos_delete(DeleteView):
	model = cat_documentos
	template_name = 'catalogos/Documentos/documentos_delete.html'
	success_url = reverse_lazy('catalogos:documentos_listar')
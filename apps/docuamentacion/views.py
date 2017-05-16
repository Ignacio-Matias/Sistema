from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView

from apps.docuamentacion.forms import *
from apps.docuamentacion.models import *
from apps.catalogos.models import *

# credenciales
def credenciales_list(request):
	credencial = credenciales.objects.all().order_by('id')
	credencial2 = credenciales.objects.filter().order_by("-id")[:4]
	tecnologia = cat_tecnologias.objects.filter().order_by("-id")[:4]
	contexto = {'credenciales':credencial, 'crede':credencial2, 'tecno':tecnologia}
	return render(request, 'documentacion/Credenciales/credenciales_list.html', contexto)

def credenciales_view(request):
	if request.method == 'POST':
		form = Credenciales_Form(request.POST)
		if form.is_valid():
			form.save()
		return redirect('documentacion:credencial_listar')
	else:
		form = Credenciales_Form()
		return render(request, 'documentacion/Credenciales/credenciales_form.html', {'form':form})

class credenciales_update(UpdateView):
	model = credenciales
	form_class = Credenciales_Form
	template_name = 'documentacion/Credenciales/credenciales_form.html'
	success_url = reverse_lazy('documentacion:credencial_listar')

class credenciales_delete(DeleteView):
	model = credenciales
	template_name = 'documentacion/Credenciales/credenciales_delete.html'
	success_url = reverse_lazy('documentacion:credencial_listar')

# ficha
def Fichas_list(request):
	ficha_li = ficha.objects.all().order_by('id')
	ficha_li2 = ficha.objects.filter().order_by("-id")[:4]
	credencial2 = credenciales.objects.filter().order_by("-id")[:4]
	contexto = {'object_list': ficha_li, 'object_list2': ficha_li2, 'crede':credencial2}
	return render(request, 'documentacion/Fichas/fichas_list.html', contexto)

class Fichas_view(CreateView):
	model = ficha
	form_class = Ficha_Form
	template_name = 'documentacion/Fichas/fichas_form.html'
	success_url = reverse_lazy('documentacion:ficha_listar')

class Fichas_update(UpdateView):
	model = ficha
	form_class = Ficha_Form
	template_name = 'documentacion/Fichas/fichas_form.html'
	success_url = reverse_lazy('documentacion:ficha_listar')

class Fichas_delete(DeleteView):
	model = ficha
	template_name = 'documentacion/Fichas/fichas_delete.html'
	success_url = reverse_lazy('documentacion:ficha_listar')

# equipo_ficha
def Equipo_Fichas_list(request):
	Eficha = equipo_ficha.objects.all().order_by('id')
	Eficha2 = equipo_ficha.objects.filter().order_by("-id")[:4]
	especialidad = equipo_ficha.objects.order_by('cat_especialidad_id_id').distinct('cat_especialidad_id_id')[:4]
	contexto = {'object_list': Eficha, 'object_list2': Eficha2, 'especialidad':especialidad}
	return render(request, 'documentacion/Equipo Ficha/equipo_ficha_list.html', contexto)

class  Equipo_Fichas_view(CreateView):
	model = equipo_ficha
	form_class = Equipo_Ficha_Form
	template_name = 'documentacion/Equipo Ficha/equipo_ficha_form.html'
	success_url = reverse_lazy('documentacion:equipo_ficha_listar')

class  Equipo_Fichas_update(UpdateView):
	model = equipo_ficha
	form_class = Equipo_Ficha_Form
	template_name = 'documentacion/Equipo Ficha/equipo_ficha_form.html'
	success_url = reverse_lazy('documentacion:equipo_ficha_listar')

class Equipo_Fichas_delete(DeleteView):
	model = equipo_ficha
	template_name = 'documentacion/Equipo Ficha/equipo_ficha_delete.html'
	success_url = reverse_lazy('documentacion:equipo_ficha_listar')

class Equipo_Ficha_search(TemplateView):
	def post(self, request, *args, **kwargs):
		buscar = request.POST['buscalo']
		#origficha = ficha.objects.get(nombre=buscar)
		#fichas = origficha.nombre_set.all()
		#fichas = ficha.objects.filter(equipo_ficha__ficha_id__nombre__istartswith=buscar)
		fichas = equipo_ficha.objects.filter(ficha_id__nombre=buscar)
		Eficha2 = equipo_ficha.objects.filter().order_by("-id")[:4]
		especialidad = equipo_ficha.objects.order_by('cat_especialidad_id_id').distinct('cat_especialidad_id_id')[:4]
		print(fichas)
		return render(request, 'documentacion/Equipo Ficha/equipo_ficha_busc.html', {'fichass':fichas, 'object_list2': Eficha2, 'especialidad':especialidad})

# ficha_cat_tecnologias
def ficha_cat_tecnologias_list(request):
	ficha_tec = ficha_cat_tecnologias.objects.all().order_by('id')
	fichatec = ficha_cat_tecnologias.objects.filter().order_by("-id")[:4]
	tecnologia = cat_tecnologias.objects.filter().order_by("-id")[:4]
	contexto = {'ficha_tecno': ficha_tec, 'fichatec': fichatec, 'tecnolo': tecnologia}
	return render(request, 'documentacion/Ficha_Tecnologias/ficha_tecnologia_list.html', contexto)

class ficha_cat_tecnologias_view(CreateView):
	model = ficha_cat_tecnologias
	form_class = Ficha_Cat_Tecnologias_Form
	template_name = 'documentacion/Ficha_Tecnologias/ficha_tecnologia_form.html'
	success_url = reverse_lazy('documentacion:ficha_tecnologia_listar')

class ficha_cat_tecnologias_update(UpdateView):
	model = ficha_cat_tecnologias
	form_class = Ficha_Cat_Tecnologias_Form
	template_name = 'documentacion/Ficha_Tecnologias/ficha_tecnologia_form.html'
	success_url = reverse_lazy('documentacion:ficha_tecnologia_listar')

class ficha_cat_tecnologias_delete(DeleteView):
	model = ficha_cat_tecnologias
	template_name = 'documentacion/Ficha_Tecnologias/ficha_tecnologia_delete.html'
	success_url = reverse_lazy('documentacion:ficha_tecnologia_listar')

# documento_archivo
def documento_archivo_list(request):
	documento = documento_archivo.objects.all().order_by('id')
	documento2 = documento_archivo.objects.filter().order_by("-id")[:4]
	ficha = documento_archivo.objects.order_by('ficha_id').distinct('ficha_id')[:4]
	contexto = {'documentos': documento, 'documentos2':documento2, 'ficha':ficha}
	return render(request, 'documentacion/Documentos/documento_list.html', contexto)

class documento_archivo_view(CreateView):
	model = documento_archivo
	form_class = Documento_Archivo_Form
	template_name = 'documentacion/Documentos/documento_form.html'
	success_url = reverse_lazy('documentacion:documento_listar')

class documento_archivo_update(UpdateView):
	model = documento_archivo
	form_class = Documento_Archivo_Form
	template_name = 'documentacion/Documentos/documento_form.html'
	success_url = reverse_lazy('documentacion:documento_listar')

class documento_archivo_delete(DeleteView):
	model = documento_archivo
	template_name = 'documentacion/Documentos/documento_delete.html'
	success_url = reverse_lazy('documentacion:documento_listar')

# logtable
def logtable_list(request):
	logtab = logtable.objects.all().order_by('id')
	logtab2 = logtable.objects.filter().order_by("-id")[:4]
	contexto = {'logtable': logtab, 'logtable2':logtab2}
	return render(request, 'documentacion/Logtable/logtable_list.html', contexto)

class logtable_view(CreateView):
	model = logtable
	form_class = Logtable_Form
	template_name = 'documentacion/Logtable/logtable_form.html'
	success_url = reverse_lazy('documentacion:logtable_listar')

class logtable_update(UpdateView):
	model = logtable
	form_class = Logtable_Form
	template_name = 'documentacion/Logtable/logtable_form.html'
	success_url = reverse_lazy('documentacion:logtable_listar')

class logtable_delete(DeleteView):
	model = logtable
	template_name = 'documentacion/Logtable/logtable_delete.html'
	success_url = reverse_lazy('documentacion:logtable_listar')
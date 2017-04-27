from django import forms

from apps.catalogos.models import *

class Cat_Tipo_Form(forms.ModelForm):

	class Meta:
		model = cat_tipo

		fields = [
			'descripcion',
		]
		labels = {
			'descripcion': 'Descripcion',
		}
		widgets = {
			'descripcion': forms.Textarea(attrs={'class':'form-control'}),
		}

class Cat_Tecnologias_Form(forms.ModelForm):

	class Meta:
		model = cat_tecnologias

		fields = [
			'descripcion',
			'tipo_id',
		]
		labels = {
			'descripcion': 'Descripcion',
			'tipo_id': 'Tipo ID',
		}
		widgets = {
			'descripcion': forms.Textarea(attrs={'class':'form-control'}),
			'tipo_id': forms.Select(attrs={'class':'form-control'}),
		}

class Cat_personas_Form(forms.ModelForm):

	class Meta:
		model = cat_personas

		fields = [
			'puc_id',
			'tipo',
		]
		labels = {
			'puc_id': 'ID',
			'tipo': 'Tipo',
		}
		widgets = {
			'puc_id': forms.TextInput(attrs={'class':'form-control'}),
			'tipo': forms.Select(attrs={'class':'form-control'}),
		}

class Cat_Especialidad_Form(forms.ModelForm):

	class Meta:
		model = cat_especialidad

		fields = [
			'descripcion',
		]
		labels = {
			'descripcion': 'Descripcion',
		}
		widgets = {
			'descripcion': forms.Textarea(attrs={'class':'form-control'}),
		}

class Cat_Estatus_Form(forms.ModelForm):

	class Meta:
		model = cat_estatus

		fields = [
			'descripcion',
		]
		labels = {
			'descripcion': 'Descripcion',
		}
		widgets = {
			'descripcion': forms.Textarea(attrs={'class':'form-control'}),
		}

class Cat_Documentos_Form(forms.ModelForm):

	class Meta:
		model = cat_documentos

		fields = [
			'archivoDescripcion',
		]
		labels = {
			'archivoDescripcion': 'Documento',
		}
		widgets = {
			'archivoDescripcion': forms.FileInput(attrs={'class': 'form-control'}),
		}
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
from django import forms

from apps.docuamentacion.models import *

# credenciales
class Credenciales_Form(forms.ModelForm):

	class Meta:
		model = credenciales

		fields = [
			'cat_tipo_id',
            'usuario',
            'contraseña',
            'host',
            'nombre',
            'puerto',
		]
		widgets = {
			'cat_tipo_id': forms.Select(attrs={'class':'form-control'}),
            'usuario': forms.TextInput(attrs={'class': 'form-control'}),
            'contraseña': forms.PasswordInput(attrs={'class': 'form-control'}),
            'host': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'puerto': forms.TextInput(attrs={'class': 'form-control'}),
		}

# ficha
class Ficha_Form(forms.ModelForm):

	class Meta:
		model = ficha

		fields = [
			'nombre',
            'descripcion',
            'cat_estatus_id',
            'url',
            'git',
            'contacto_id',
            'tipouso',
            'dependencia_id',
            'credencial_id',
		]
		widgets = {
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'cat_estatus_id': forms.Select(attrs={'class': 'form-control'}),
            'url': forms.TextInput(attrs={'class': 'form-control'}),
            'git': forms.TextInput(attrs={'class': 'form-control'}),
            'contacto_id': forms.Select(attrs={'class': 'form-control'}),
            'tipouso': forms.Select(attrs={'class': 'form-control'}),
            'dependencia_id': forms.TextInput(attrs={'class': 'form-control'}),
            'credencial_id': forms.CheckboxSelectMultiple(),
		}

# equipo_ficha
class Equipo_Ficha_Form(forms.ModelForm):

	class Meta:
		model = equipo_ficha

		fields = [
			'ficha_id',
            'cat_personas_id',
            'cat_especialidad_id',
		]
		widgets = {
			'ficha_id': forms.Select(attrs={'class':'form-control'}),
            'cat_personas_id': forms.Select(attrs={'class': 'form-control'}),
            'cat_especialidad_id': forms.Select(attrs={'class': 'form-control'}),
		}

# ficha_cat_tecnologias
class Ficha_Cat_Tecnologias_Form(forms.ModelForm):

	class Meta:
		model = ficha_cat_tecnologias

		fields = [
			'ficha_id',
            'cat_tecnologias_id',
            'version',
		]
		widgets = {
			'ficha_id': forms.Select(attrs={'class':'form-control'}),
            'cat_tecnologias_id': forms.Select(attrs={'class': 'form-control'}),
            'version': forms.TextInput(attrs={'class': 'form-control'}),
		}

# documento_archivo
class Documento_Archivo_Form(forms.ModelForm):

	class Meta:
		model = documento_archivo

		fields = [
			'ficha_id',
            'cat_documento_id',
		]
		widgets = {
			'ficha_id': forms.Select(attrs={'class':'form-control'}),
            'cat_tecnologias_id': forms.Select(attrs={'class': 'form-control'}),
		}

# logtable
class Logtable_Form(forms.ModelForm):

	class Meta:
		model = logtable

		fields = [
			'usuario_id',
            'fecha',
            'nametabla',
            'registro_id',
            'tipomovimiento',
		]



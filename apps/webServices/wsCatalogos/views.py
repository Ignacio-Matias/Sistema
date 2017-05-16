# Create your views here.
from django.http import HttpResponse
from apps.catalogos.models import cat_tipo
# Integramos la serializacion de los objetos
from django.core import serializers



def wsCatalogos_view(request):
	data = serializers.serialize("json",cat_tipo.objects.all().order_by('id'))
	# Retorna la informacion en formato json
	return HttpResponse(data,content_type ='application/json')
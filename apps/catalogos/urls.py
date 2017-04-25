from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from apps.catalogos.views import *

urlpatterns = [
    url(r'^tipo/listar', login_required(catalogo_list.as_view()), name='catalogo_listar'),
    url(r'^tipo/nuevo', login_required(catalogo_view), name='catalogo_nuevo'),
    url(r'^tipo/editar/(?P<pk>\d+)/$', login_required(catalogo_update.as_view()), name='catalogo_editar'),
    url(r'^tipo/eliminar/(?P<pk>\d+)/$', login_required(catalogo_delete.as_view()), name='catalogo_eliminar'),
    url(r'^tecnologias/listar', login_required(tecnologia_list), name='tecnologia_listar'),
    url(r'^tecnologias/nuevo', login_required(tecnologia_view), name='tecnologia_nuevo'),
    url(r'^tecnologias/editar/(?P<pk>\d+)/$', login_required(tecnologia_update.as_view()), name='tecnologia_editar'),
]
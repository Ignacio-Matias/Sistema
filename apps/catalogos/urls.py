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
    url(r'^tecnologias/eliminar/(?P<pk>\d+)/$', login_required(tecnologia_delete.as_view()), name='tecnologia_eliminar'),
    url(r'^personas/listar', login_required(persona_list), name='persona_listar'),
    url(r'^personas/nuevo', login_required(persona_view), name='persona_nuevo'),
    url(r'^personas/editar/(?P<pk>\d+)/$', login_required(persona_update.as_view()), name='persona_editar'),
    url(r'^personas/eliminar/(?P<pk>\d+)/$', login_required(persona_delete.as_view()), name='persona_eliminar'),
    url(r'^especialidades/listar', login_required(especialidad_list), name='especialidad_listar'),
    url(r'^especialidades/nuevo', login_required(especialidad_view), name='especialidad_nuevo'),
    url(r'^especialidades/editar/(?P<pk>\d+)/$', login_required(especialidad_update.as_view()), name='especialidad_editar'),
    url(r'^especialidades/eliminar/(?P<pk>\d+)/$', login_required(especialidad_delete.as_view()), name='especialidad_eliminar'),
    url(r'^estatus/listar', login_required(estatus_list), name='estatus_listar'),
    url(r'^estatus/nuevo', login_required(estatus_view), name='estatus_nuevo'),
    url(r'^estatus/editar/(?P<pk>\d+)/$', login_required(estatus_update.as_view()), name='estatus_editar'),
    url(r'^estatus/eliminar/(?P<pk>\d+)/$', login_required(estatus_delete.as_view()), name='estatus_eliminar'),
    url(r'^documentos/listar', login_required(documentos_list), name='documentos_listar'),
    url(r'^documentos/nuevo', login_required(documentos_view), name='documentos_nuevo'),
    url(r'^documentos/editar/(?P<id>\d+)/$', documentos_update, name='documentos_editar'),
    url(r'^documentos/eliminar/(?P<pk>\d+)/$', login_required(documentos_delete.as_view()), name='documentos_eliminar'),

]
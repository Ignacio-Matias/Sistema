from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from apps.docuamentacion.views import *

urlpatterns = [
    # credenciales
    url(r'^credenciales/listar', login_required(credenciales_list), name='credencial_listar'),
    url(r'^credenciales/nuevo', login_required(credenciales_view), name='credencial_nuevo'),
    url(r'^credenciales/editar/(?P<pk>\d+)/$', login_required(credenciales_update.as_view()), name='credencial_editar'),
    url(r'^credenciales/eliminar/(?P<pk>\d+)/$', login_required(credenciales_delete.as_view()), name='credencial_eliminar'),
    # fichas
    url(r'^fichas/listar', login_required(Fichas_list.as_view()), name='ficha_listar'),
    url(r'^fichas/nuevo', login_required(Fichas_view.as_view()), name='ficha_nuevo'),
    url(r'^fichas/editar/(?P<pk>\d+)/$', login_required(Fichas_update.as_view()), name='ficha_editar'),
    url(r'^fichas/eliminar/(?P<pk>\d+)/$', login_required(Fichas_delete.as_view()), name='ficha_eliminar'),
    # equipo
    url(r'^equipo-ficha/listar', login_required(Equipo_Fichas_list.as_view()), name='equipo_ficha_listar'),
    url(r'^equipo-ficha/nuevo', login_required(Equipo_Fichas_view.as_view()), name='equipo_ficha_nuevo'),
    url(r'^equipo-ficha/editar/(?P<pk>\d+)/$', login_required(Equipo_Fichas_update.as_view()), name='equipo_ficha_editar'),
    url(r'^equipo-ficha/eliminar/(?P<pk>\d+)/$', login_required(Equipo_Fichas_delete.as_view()), name='equipo_ficha_eliminar'),
    # ficha tecnologias
    url(r'^ficha-tecnologia/listar', login_required(ficha_cat_tecnologias_list), name='ficha_tecnologia_listar'),
    url(r'^ficha-tecnologia/nuevo', login_required(ficha_cat_tecnologias_view.as_view()), name='ficha_tecnologia_nuevo'),
    url(r'^ficha-tecnologia/editar/(?P<pk>\d+)/$', login_required(ficha_cat_tecnologias_update.as_view()), name='ficha_tecnologia_editar'),
    url(r'^ficha-tecnologia/eliminar/(?P<pk>\d+)/$', login_required(ficha_cat_tecnologias_delete.as_view()), name='ficha_tecnologia_eliminar'),
    # documento
    url(r'^documento/listar', login_required(documento_archivo_list), name='documento_listar'),
    url(r'^documento/nuevo', login_required(documento_archivo_view.as_view()), name='documento_nuevo'),
    url(r'^documento/editar/(?P<pk>\d+)/$', login_required(documento_archivo_update.as_view()), name='documento_editar'),
    url(r'^documento/eliminar/(?P<pk>\d+)/$', login_required(documento_archivo_delete.as_view()), name='documento_eliminar'),
    # logtable
    url(r'^logtable/listar', login_required(logtable_list), name='logtable_listar'),
    url(r'^logtable/nuevo', login_required(logtable_view.as_view()), name='logtable_nuevo'),
    url(r'^logtable/editar/(?P<pk>\d+)/$', login_required(logtable_update.as_view()), name='logtable_editar'),
    url(r'^logtable/eliminar/(?P<pk>\d+)/$', login_required(logtable_delete.as_view()), name='logtable_eliminar'),

]
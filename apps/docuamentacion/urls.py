from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from apps.docuamentacion.views import *

urlpatterns = [
    url(r'^credenciales/listar', login_required(credenciales_list), name='credencial_listar'),
    url(r'^credenciales/nuevo', login_required(credenciales_view), name='credencial_nuevo'),
    url(r'^credenciales/editar/(?P<pk>\d+)/$', login_required(credenciales_update.as_view()), name='credencial_editar'),
    url(r'^credenciales/eliminar/(?P<pk>\d+)/$', login_required(credenciales_delete.as_view()), name='credencial_eliminar'),
    url(r'^fichas/listar', login_required(Fichas_list.as_view()), name='ficha_listar'),
    url(r'^fichas/nuevo', login_required(Fichas_view.as_view()), name='ficha_nuevo'),
    url(r'^fichas/editar/(?P<pk>\d+)/$', login_required(Fichas_update.as_view()), name='ficha_editar'),
    url(r'^fichas/eliminar/(?P<pk>\d+)/$', login_required(Fichas_delete.as_view()), name='ficha_eliminar'),
    url(r'^equipo-ficha/listar', login_required(Equipo_Fichas_list.as_view()), name='equipo_ficha_listar'),
    url(r'^equipo-ficha/nuevo', login_required(Equipo_Fichas_view.as_view()), name='equipo_ficha_nuevo'),
    url(r'^equipo-ficha/editar/(?P<pk>\d+)/$', login_required(Equipo_Fichas_update.as_view()), name='equipo_ficha_editar'),
    url(r'^equipo-ficha/eliminar/(?P<pk>\d+)/$', login_required(Equipo_Fichas_delete.as_view()), name='equipo_ficha_eliminar'),
    url(r'^ficha-tecnologia/listar', login_required(ficha_cat_tecnologias_list), name='ficha_tecnologia_listar'),

]
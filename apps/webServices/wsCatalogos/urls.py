from django.conf.urls import url
from django.contrib.auth.decorators import login_required


from apps.webServices.wsCatalogos.views import *

urlpatterns = [
    url(r'^ws/catalogos/$', login_required(wsCatalogos_view), name='ws_catalogos_url'),
]
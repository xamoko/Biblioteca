from usuarios.models import *
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404
from django.conf.urls import patterns, include, url

from django.contrib import admin
from biblioteca import *

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'biblioteca.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', include('usuarios.urls')),
    url(r'^adquirir_libro/$','usuarios.views.Nuevo'),
    url(r'^devolver_libro/$','usuarios.views.D_Libro'),
    url(r'^admin/', include(admin.site.urls)),

    
    #url(r'^$',usuarios.views.index),


)

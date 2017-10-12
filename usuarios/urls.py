from usuarios.models import *
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404
from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('usuarios.views',
		url(r'^$', 'R_Libro'),

		#url(r'^usuarios/$','usuarios.views.adquirir_libro'),
		)
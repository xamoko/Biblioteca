# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from usuarios.models import *

class DatosForm(ModelForm):
	class Meta: 
		model = RegistroDatos

class RegistroLibro(ModelForm):
	class Meta:
		model = libro

class DevolucionLibro(ModelForm):
	class Meta:
		model = Devolver_libro
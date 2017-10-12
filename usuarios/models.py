# -*- coding: utf-8 -*-
from django.db import models
#from django.contrib.auth.models import User

# Create your models here.
class Datos(models.Model):
	
	clave = models.CharField(max_length=50)

	def __unicode__(self):
		return self.clave

class RegistroDatos(models.Model):
	fkDatos = models.ForeignKey(Datos)
	Nombre = models.CharField(max_length=50)
	Apellido_Paterno = models.CharField(max_length=50)
	Apellido_Materno = models.CharField(max_length=50)

	def __unicode__(self):
		return u'%s | %s ' % (self.fkDatos, self.nombre)

class Meta:
	verbose_Name=u'Introduce Datos'

class libro(models.Model):
	Matricula = models.CharField(max_length=50)
	Numero_de_Aquisicion = models.CharField(max_length=50)
	Nombre_del_Libro = models.CharField(max_length=50)
	Fecha_de_Salida = models.DateField(max_length=50)
	Entrega = models.DateField(max_length=50)

class Devolver_libro(models.Model):
	Numero_de_Control = models.CharField(max_length=50)
	Numero_de_Aquisicion = models.CharField(max_length=50)
	Salida = models.DateField()
	Entrega = models.DateField()
	Renovaciones = models.CharField(max_length=50)
	Administrativo = models.CharField(max_length=50)
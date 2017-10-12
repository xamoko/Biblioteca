#from django.shortcuts import render
from usuarios.models import *
from usuarios.forms import *
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

# Create your views here.
def index(request):
	usuarios = Datos.objects.all()
	return render_to_response('index.html', context_instance=RequestContext(request, locals()))

def ver_detalle(request, id):
	ver = get_object_or_404(Datos, id=id)
	return render_to_response('usuario/ver.html', context_instance=RequestContext(request, locals()))

def adquirir_libro(request):
	Libro = libro.objects.all()



	return render_to_response('adquirir_libro.html', context_instance=RequestContext(request, locals()))

def devolver_libro(request):
	devolver_libr = Devolver_libro.objects.all()
	return render_to_response('devolver_libro.html', context_instance=RequestContext(request, locals()))

def Nuevo(request):
	
	if request.method=='POST':
		formulario = DatosForm(request.POST) #formulario es una variable y DatosForm es el nombre de la clase declarada en forms.py 

		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('adquirir_libro/')

	else:
		formulario = DatosForm()
	
	return render_to_response('adquirir_libro.html',{'formulario':formulario}, context_instance=RequestContext(request))

def R_Libro(request):

	if request.method=='POST':
		registro = RegistroLibro(request.POST)

		if registro.is_valid():
			registro.save()
			return HttpResponseRedirect('/')

	else:
		registro = RegistroLibro()

	return render_to_response('index.html',{'registro':registro}, context_instance=RequestContext(request))

def D_Libro(request):
	if request.method=='POST':
		devolucion = DevolucionLibro(request.POST)

		if devolucion.is_valid():
			devolucion.save()
			return HttpResponseRedirect('devolver_libro/')
	else:
		devolucion = DevolucionLibro()
	return render_to_response('devolver_libro.html',{'devolucion':devolucion}, context_instance=RequestContext(request))

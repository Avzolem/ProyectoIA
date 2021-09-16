from django.http import HttpResponse
from django.template import Template, Context
import datetime

def saludo(request):
   nombre="Andres"
   apellido="Aguilar"

   doc_externo = open ("C:/Users/Avsolem/Documents/Proyectos_django/miprimerproyecto/ProyectoIA/miprimerproyecto/miplantilla.html") 
   plt = Template(doc_externo.read())
   doc_externo.close()

   ctx = Context({"nombre_persona":nombre, "apellido_persona": apellido})

   documento=plt.render(ctx)

   return(HttpResponse("<html><body><h1>hola mundo</h1></body></html>"))

def damefecha(request):
   fecha_actual=datetime.datetime.now()
   documento = """
               <html>
               <body>
               <h1>
               Fecha y hora actuales %s
               </h1>
               </body>
               </html>
               """ %fecha_actual
   return HttpResponse(documento)

def calcularedad(request,anio):
   edadActual=18
   periodo=anio-2021
   edadfutura=edadActual+periodo
   documento = """
                <html>
               <body>
               <h2>
               En el año %s tendras %s años
               </h2>
               </body>
               </html>
               """  %(anio,edadfutura)
   return HttpResponse(documento)

def Calcularedad(request,edad,anio):
   periodo=anio-2021
   edadfutura=edad+periodo
   documento = """
                <html>
               <body>
               <h2>
               En el año %s tendras %s años
               </h2>
               </body>
               </html>
               """  %(anio,edadfutura)
   return HttpResponse(documento)
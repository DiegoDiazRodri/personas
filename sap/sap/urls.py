from django.contrib import admin
from django.urls import path
from webapp.views import bienvenido
from personas.views import detallePersona, detalleDomicilio, editarDomicilio, eliminarDomicilio, nuevoDomicilio
from personas.views import nuevaPersona
from personas.views import editarPersona
from personas.views import eliminarPersona

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('bienvenido/', bienvenido),
    path('', bienvenido, name='index'),
    path('detalle_persona/<int:id>', detallePersona),
    path('nueva_persona', nuevaPersona),
    path('editar_persona/<int:id>', editarPersona),
    path('eliminar_persona/<int:id>', eliminarPersona),

    path('detalle_domicilio/<int:id>', detalleDomicilio),
    path('nuevo_domicilio', nuevoDomicilio),
    path('editar_domicilio/<int:id>', editarDomicilio),
    path('eliminar_domicilio/<int:id>', eliminarDomicilio),
]

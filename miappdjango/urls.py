"""miappdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.miapp, name='miapp')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='miapp')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from miapp import views
#import miapp
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('contacto/', views.contacto, name="contacto"),
    path('productos/', views.listadoProductos, name="listado"),
    path('plantilla/', views.muestraPlantilla, name="plantilla"),
    path('datos/', views.muestraDatos, name="datos"),
    path('captura/<int:n>', views.capturaDatos, name='captura'),
    path('captura/<str:cadena>', views.capturaCadena, name='captura-cadena'),
    path('articulos/<int:agno>/<int:mes>', views.capturaFecha, name='captura-fecha'),
    path('incluye/', views.incluyePlantilla, name="incluye-plantilla")
]

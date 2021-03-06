"""IngSoftware URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import MedicoView, PerfilView, SignInView, SignOutView, SignUpView, UploadToMammoView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path(
        'admin/',
        admin.site.urls
    ),
    #URL PRINCIPAL
    path(
        route='',
        view=MedicoView.as_view(),
        name='index'
    ),
    path(
        'upload/',
        UploadToMammoView,
        name='upload'
        ),
    path('perfil/',PerfilView.as_view(), name='perfil'),
    path('registrate/', SignUpView.as_view(), name='sign_up'),
    path('incia-sesion/', SignInView.as_view(), name='sign_in'),
    path('cerrar-sesion/', SignOutView.as_view(), name='sign_out'),
    ]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

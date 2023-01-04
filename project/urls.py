from django.db import models
 
"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.static import static 
from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path
from ambientalnews.views import(index, PostListar, PostCrear, 
                             PostBorrar, PostActualizar, PostDetalle,
                             UserSignUp, UserLogin, UserLogout, AvatarActualizar, UserActualizar,
                             MensajeCrear, MensajeListar, MensajeDetalle)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('succes_update_message/', TemplateView.as_view(template_name= 'ejemplo/succes_update_message.html')),
    path('ambientalnews/', index, name='inicio'),
    path('ambientalnews/listar/', PostListar.as_view(), name='listar'),
    path('ambientalnews/crear/', PostCrear.as_view(), name='post-crear'),
    path('ambientalnews/borrar/<int:pk>', PostBorrar.as_view(), name='post-borrar' ),
    path('ambientalnews/actualizar/<int:pk>', PostActualizar.as_view(), name='post-actualizar'),
    path('ambientalnews/<int:pk>/detalle/', PostDetalle.as_view(), name= 'post-detalle'),
    path('ambientalnews/signup/',UserSignUp.as_view(), name= 'signup' ),
    path('ambientalnews/login/', UserLogin.as_view(), name='login'),
    path('ambientalnews/logout/', UserLogout.as_view(), name='logout'),
    path('ambientalnews/avatars/<int:pk>/actualizar/', AvatarActualizar.as_view(), name='avatar-actualizar'),
    path('ambientalnews/users/<int:pk>/actualizar/', UserActualizar.as_view(), name='user-actualizar' ),
    path('ambientalnews/mensajes/crear/', MensajeCrear.as_view(), name='crear-mensaje'),
    path('ambientalnews/mensajes/<int:pk>/detalle/', MensajeDetalle.as_view(), name='detalle-mensaje'),
    path('ambientalnews/mensajes/listar/', MensajeListar.as_view(), name='listar-mensaje'),
]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)








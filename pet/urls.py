#Pet urls
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, logout_then_login


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('apps.mascota.urls', 'index'))),
    path('mascota/', include('apps.mascota.urls')),
    path('adopcion/', include('apps.adopcion.urls')),
    path('usuario/', include('apps.usuario.urls')),
    path('accounts/login/', LoginView.as_view(template_name='index.html'), name="login"),
    path('logout', logout_then_login, name='logout'),
    ]

from django.contrib import admin
from django.urls import path, include
from sistema.views import Login, Logout, LoginApi
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Login.as_view(), name='login'),
    #path('autenticacao-api/', obtain_auth_token),
    path('autenticacao-api/', LoginApi.as_view()),
    path('logout/', Logout.as_view(), name='logout'),
    path('veiculo/', include('veiculo.urls'), name='veiculo'),
    path('anuncio/', include('anuncio.urls'), name='anuncio')
]

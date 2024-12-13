from django.contrib import admin
from django.urls import path
from prueba4App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),
    path('admin_page/', views.admin_page, name='admin_page'),
    path('user/', views.user_page, name='user_page'),
    path('agregar_cliente/', views.agregar_cliente, name='agregar_cliente'),
    path('clientes_listado/', views.admin_listado_clientes, name='admin_clientes'),
    path('buscar/', views.admin_buscar, name='admin_buscar'),
    path('eliminar/', views.admin_eliminar, name='admin_eliminar'),
    path('user_buscar/', views.user_buscar, name='user_buscar'),
]

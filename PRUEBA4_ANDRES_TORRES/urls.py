from django.contrib import admin
from django.urls import path
from prueba4App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),
    path('admin_page/', views.admin_page, name='admin_page'),
    path('user/', views.user_page, name='user_page'),
]

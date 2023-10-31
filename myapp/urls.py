from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('reset_password/', views.reset_password, name="reset_password"),
    path('cliente/', views.Client_view.client, name="cliente"),
    path('nuevo-cliente/', views.Client_view.new_client, name="new_client"),
    path('trazabilidad/', views.trazability, name="trazability"),
    path('maquinaria/', views.Machine_view.machine, name="maquinaria"),
    path('nueva_maquinaria/', views.Machine_view.new_machine, name="nueva_maquinaria"),
    path('manuales/', views.Manual_view.manual, name="Manuales"),
    path('nuevo_manual/', views.Manual_view.new_manual, name="nuevo_manual"),
    ]
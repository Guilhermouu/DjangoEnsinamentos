from django.urls import path
from . import views
urlpatterns=[
    path('ver/', views.ver_produto, name="ver_produto"),
    path('inserir_produto', views.inserir_produto, name="inserir_produto")
]
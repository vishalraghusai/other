from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('extend/', views.extend ,name = 'ex'),
    path('indexpage/', views.index,  name='index'),
    path('formpage/', views.form_name, name='form_name'),
    path('another/', views.another_page, name= 'another')

]
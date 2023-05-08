from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("registration/",views.registration),
    path("login/",views.login),
    path("user_login/",views.user_login),
    path("welcome/",views.welcome),
    path("table/",views.table),
    path("update/<int:uid>/",views.update),
    path("update_data/",views.update),
    path("delete/",views.delete),

 ]
 

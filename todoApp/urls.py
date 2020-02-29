from django.urls import path
from . import views


urlpatterns = [
    
    path('',  views.home, name = "todo-home"),
    path('about/',  views.about, name = "todo-about"),
    path('delete/<int:pk>/',  views.delete, name = "todo-delete"),
    path('update/<int:pk>/',  views.update, name = "todo-update"),
    path('login/',  views.login, name = "todo-login"), # Later upgrade
    path('register',  views.register, name = "todo-register"), # Later upgrade 


]    
   
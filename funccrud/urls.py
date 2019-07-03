from django.urls import path
from django.urls import path, include
from . import views
import funccrud.urls
import funccrud.views

urlpatterns = [

    path('', views.read, name="home"),
    path('newblog/', views.create, name="newblog"),
    path('update/<int:pk>', views.update, name="update"),
    path('delete/<int:pk>', views.delete, name="delete"),
  
   
]
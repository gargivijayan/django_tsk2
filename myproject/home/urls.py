from django.contrib import admin
from django.urls import path
from . import views
urlpatterns=[
    
    path("",views.front)  ,
    path('index', views.index),
    path('save',views.save),
    path('delete/<id>', views.delete),
    path('edit/<id>',views.edit),
    path('update/<id>', views.update),
    path('view/<eid>', views.view),

    
       
]

from django.urls import path
from .import views

urlpatterns=[
    path('',views.f1,name='f1'),
]
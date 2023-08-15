
from django.urls import path

from app1 import views

urlpatterns = [
    path('',views.index,name='index'),

    path('register/',views.register,name='register'),
    path('register1',views.register,name='register'),
]

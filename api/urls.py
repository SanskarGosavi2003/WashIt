from django.urls import path
from . import views

urlpatterns = [
    path('',views.printer),
    path('add/',views.addStu)
]
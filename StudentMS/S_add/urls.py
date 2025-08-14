from django.urls import path
from S_add import views

urlpatterns = [
    path('S_add/', views.S_add, name='S_add'),
] 
from django.urls import path
from S_list import views
urlpatterns = [
    path('', views.S_list, name='S_list'),
]
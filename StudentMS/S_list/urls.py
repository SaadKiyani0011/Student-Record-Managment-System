from django.urls import path
from S_list.views import (
    StudentListView,
    StudentCreateView,
    StudentUpdateView,
    StudentDeleteView
)

urlpatterns = [
    path('', StudentListView.as_view(), name='S_list'),
    path('add/', StudentCreateView.as_view(), name='S_add'),
    path('<int:pk>/edit/', StudentUpdateView.as_view(), name='S_edit'),
    path('<int:pk>/delete/', StudentDeleteView.as_view(), name='S_delete'),
]
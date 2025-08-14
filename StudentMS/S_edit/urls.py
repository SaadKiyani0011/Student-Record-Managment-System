from django.urls import path
from S_edit import views
urlpatterns = [
    path('S_edit/', views.S_edit, name='S_edit'),
]
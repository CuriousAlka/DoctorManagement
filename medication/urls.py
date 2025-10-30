from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='medication_list'),
    path('add/', views.create, name='medication_add'),
    path('edit/<int:medication_id>/', views.edit, name='medication_edit'),
    path('delete/<int:medication_id>/', views.delete, name='medication_delete'),
]

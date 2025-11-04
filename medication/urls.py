from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='medication_list'),
    path('create/', views.create, name='medication_create'),
    path('view/<int:medication_id>/', views.view, name='medication_view'),
    path('edit/<int:medication_id>/', views.edit, name='medication_edit'),
    path('delete/<int:medication_id>/', views.delete, name='medication_delete'),
]

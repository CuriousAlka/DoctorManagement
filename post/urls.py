from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),            # List view
    path('create/', views.post_create, name='post_create'), # Create
    path('<int:pk>/', views.post_view, name='post_view'),   # Detail view
    path('<int:pk>/edit/', views.post_edit, name='post_edit'), # Edit
    path('<int:pk>/delete/', views.post_delete, name='post_delete'), # Delete
]

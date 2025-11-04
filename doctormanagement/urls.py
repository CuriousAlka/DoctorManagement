from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),  # 👈 Homepage → users app
    path('post/', include('post.urls')),
    path('medication/', include('medication.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

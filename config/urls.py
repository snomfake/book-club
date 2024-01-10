from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("registration/", include("registration.urls")),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path("", include("social_django.urls", namespace="social")),
    path("", include("books.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

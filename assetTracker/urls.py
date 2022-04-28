from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('assets/', include('assets.urls')),
    path('admin/', admin.site.urls),
]

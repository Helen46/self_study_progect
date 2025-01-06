from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('courses/', include('courses.urls', namespace='courses')),
    path('users/', include('users.urls', namespace='users')),
    path('users_tests/', include('users_tests.urls', namespace='users_tests')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

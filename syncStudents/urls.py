from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('', include('apps.home.urls', namespace='home')),
	path('students/', include('apps.students.urls', namespace='students')),
    path('admin/', admin.site.urls),
]

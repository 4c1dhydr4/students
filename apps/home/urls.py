from django.urls import path, include
from apps.home.views import index

app_name = 'home'

urlpatterns = [
    path('', index, name='index'),
]

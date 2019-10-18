from django.urls import path, include
from apps.students.views import index, myProfile, myNotes, myCourses

app_name = 'students'

urlpatterns = [
    path('', index, name='index'),
    path('profile/', myProfile, name='my_profile'),
    path('notes/', myNotes, name='my_notes'),
    path('courses/', myCourses, name='my_courses'),
]

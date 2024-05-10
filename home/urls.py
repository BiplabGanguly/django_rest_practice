from django.urls import path
from .views import *

urlpatterns = [
    path('index/',home),
    path('home/',studentDetails.as_view()),
    path('count/',total_student.as_view()),
]
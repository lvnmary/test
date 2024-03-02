from django.urls import path
from .views import CourseListAPIView

urlpatterns = [
    path('api/courses/', CourseListAPIView.as_view(), name='course-list'),
]

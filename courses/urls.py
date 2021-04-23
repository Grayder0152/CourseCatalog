from .views import ListCoursesAPIView, DetailCourseAPIView

from django.urls import path

urlpatterns = [
    path('courses/', ListCoursesAPIView.as_view(), name='courses_list'),
    path('courses/<int:pk>', DetailCourseAPIView.as_view(), name='course_by_id'),
    path('courses/<str:title>', ListCoursesAPIView.as_view(), name='course_by_title'),
]

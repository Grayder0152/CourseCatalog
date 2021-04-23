from .views import ListCoursesAPIView, DetailCourseAPIView

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('courses/', ListCoursesAPIView.as_view(), name='courses_list'),
    path('courses/<int:pk>', DetailCourseAPIView.as_view(), name='course_by_id'),
    path('courses/<str:title>', ListCoursesAPIView.as_view(), name='course_by_title'),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

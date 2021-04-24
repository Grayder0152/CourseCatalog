from .models import Course
from .serializers import (
    ListCoursesSerializer,
    DetailCourseSerializer
)

import datetime

from django.http import HttpResponse
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404


def format_date(date):
    """The function for formatting date for API filter"""
    date = tuple(map(int, date.split('-')))
    date = datetime.date(*date)
    return date


def index(request):
    """The function for rendering index page"""
    return HttpResponse(
        """
        <h1>
            <a href="/api/courses">API for courses catalog</a>
        </h1>
        """
    )


class ListCoursesAPIView(APIView):
    def get(self, request, title=None):
        """The method returns a list of all courses"""
        courses = Course.objects.all()
        if title is not None:
            courses = Course.objects.filter(title__icontains=title)

        if request.query_params:
            if request.query_params.get('date_start') is not None:
                date_start = format_date(request.query_params.get('date_start'))
            else:
                date_start = datetime.datetime.today().date()

            if request.query_params.get('date_end') is not None:
                date_end = format_date(request.query_params.get('date_end'))
            else:
                date_end = Course.objects.order_by('-date_end').first().date_end
            courses = Course.objects.filter(
                Q(date_start__gte=date_start) & Q(date_start__lte=date_end)
            )

        serializer = ListCoursesSerializer(courses, many=True)
        return Response(serializer.data)

    def post(self, request):
        """The method creates a new course"""
        course = request.data
        serializer = DetailCourseSerializer(data=course)
        if serializer.is_valid(raise_exception=True):
            course_saved = serializer.save()
        return Response({
            "success": f"Course '{course_saved.title}' created successfully"
        })


class DetailCourseAPIView(APIView):
    def get(self, request, pk):
        """The method returns detailed information about the selected course"""
        course = get_object_or_404(Course.objects.all(), pk=pk)
        serializer = DetailCourseSerializer(course)
        return Response(serializer.data)

    def put(self, request, pk):
        """The method changes course fields"""
        saved_course = get_object_or_404(Course.objects.all(), pk=pk)
        data = request.data
        serializer = DetailCourseSerializer(
            instance=saved_course,
            data=data,
            partial=True
        )
        if serializer.is_valid(raise_exception=True):
            course_saved = serializer.save()
        return Response({
            "success": f"Course '{course_saved.title}' updated successfully"
        })

    def delete(self, request, pk):
        """The method deletes the selected course"""
        course = get_object_or_404(Course.objects.all(), pk=pk)
        course.delete()
        return Response({
            "message": f"Course with id '{pk}' has been deleted."
        }, status=204)

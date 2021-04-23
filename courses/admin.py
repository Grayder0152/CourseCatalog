from .models import Course

from django.contrib import admin


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    """Admin for course"""
    exclude = ('id', )


admin.site.site_title = 'Courses catalog'
admin.site.site_header = 'Courses catalog'

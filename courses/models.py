from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=120, verbose_name="Title")
    date_start = models.DateField(verbose_name="Start date")
    date_end = models.DateField(verbose_name="End date")
    count_lectures = models.PositiveSmallIntegerField(verbose_name="Count lectures")

    def __str__(self):
        return f"Course '{self.title}'"


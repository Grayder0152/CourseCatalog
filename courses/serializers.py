from .models import Course

from rest_framework import serializers


class ListCoursesSerializer(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(required=False, read_only=True)
    title = serializers.CharField(max_length=120)


class DetailCourseSerializer(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(required=False, read_only=True)
    title = serializers.CharField(max_length=120)
    date_start = serializers.DateField()
    date_end = serializers.DateField()
    count_lectures = serializers.IntegerField()

    def create(self, validated_data):
        return Course.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.date_start = validated_data.get('date_start', instance.date_start)
        instance.date_end = validated_data.get('date_end', instance.date_end)
        instance.count_lectures = validated_data.get('count_lectures', instance.count_lectures)
        instance.save()
        return instance

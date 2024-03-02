from rest_framework import serializers
from .models import Course


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()

    def get_lesson_count(self, course):
        return course.lessons.count()

    class Meta:
        model = Course
        fields = (
            'id',
            'title',
            'start_date',
            'price',
            'min_group_users',
            'max_group_users',
            'lesson_count'
        )

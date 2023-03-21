from rest_framework import serializers
from .models import Subject
from .models import Student
from .models import GPA


class SubjectSerializer(serializers.HyperlinkedModelSerializer):
    subjects = serializers.HyperlinkedIdentityField(
        many=True,
        read_only=True,
        view_name='subject-detail'
    )

    class Meta:
        model = Subject
        fields = (
            'url',
            'pk',
            'name',
            'subjects'
        )


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    students = serializers.HyperlinkedIdentityField(
        many=True,
        read_only=True,
        view_name='student-detail'
    )

    class Meta:
        model = Student
        fields = (
            'url',
            'pk',
            'name',
            'surname',
            'students'
        )


class GPASerializer(serializers.ModelSerializer):
    student = serializers.SlugRelatedField(queryset=Student.objects.all(), slug_field='name')
    subject = serializers.SlugRelatedField(queryset=Subject.objects.all(), slug_field='name')

    class Meta:
        model = GPA
        fields = (
            'url',
            'pk',
            'student',
            'subject',
            'gpa'
        )

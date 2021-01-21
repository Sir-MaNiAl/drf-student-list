from rest_framework import serializers

from api.models import Student


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ['id', 'surname', 'name', 'patronymic', 'birthday', 'grade']

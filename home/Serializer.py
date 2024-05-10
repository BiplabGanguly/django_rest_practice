from rest_framework import serializers
from . import models

class StudentSerializer(serializers.Serializer):
    student_name = serializers.CharField()
    student_age = serializers.IntegerField()


    def validate(self, data):
        if data['student_age'] < 18:
            raise serializers.ValidationError("Age must be 18 or older.")
        return data

    def create(self, validated_data):
        student_details = models.StudentModel.objects.create(**validated_data)
        student_details.save()
        return validated_data


class StudentCountSerializer(serializers.Serializer):
    total_student = serializers.IntegerField()
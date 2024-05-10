from rest_framework import serializers
from . import models
import re

class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    student_name = serializers.CharField()
    student_age = serializers.IntegerField()


    def validate(self, data):
        if data['student_age'] < 18:
            raise serializers.ValidationError("Age must be 18 or older.")
        
        special_chars_pattern = r'[^a-zA-Z0-9\s]'
        if re.search(special_chars_pattern,data['student_name']):
            raise serializers.ValidationError("no special character allowed")
        return data
    

    def create(self, validated_data):
        student_details = models.StudentModel.objects.create(**validated_data)
        student_details.save()
        return validated_data
    

    def update(self, instance, validated_data):
        instance.student_name = validated_data.get('student_name', instance.student_name)
        instance.student_age = validated_data.get('student_age', instance.student_age)
        instance.save()
        return instance


class StudentCountSerializer(serializers.Serializer):
    total_student = serializers.IntegerField()

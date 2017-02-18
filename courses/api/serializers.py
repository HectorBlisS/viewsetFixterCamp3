from rest_framework import serializers
from ..models import Subject, Course
from django.contrib.auth.models import User


class SubjectSerializer(serializers.ModelSerializer):
	class Meta:
		model = Subject
		fields = ('id','title','slug')


class CourseSerializer(serializers.ModelSerializer):
	class Meta:
		model = Course
		fields = ('id','subject','alumni')

class AlumniSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id','username')
		

class CursoSerializer(serializers.ModelSerializer):
	subject = SubjectSerializer(many=False)
	alumni = AlumniSerializer(many=True)

	class Meta:
		model = Course
		fields = ('id','subject','alumni')

	def create(self, validated_data):
		dic = validated_data.pop('subject')
		subject = Subject.objects.get(slug=dic['slug'])
		course = Course.objects.create(subject=subject)
		return course
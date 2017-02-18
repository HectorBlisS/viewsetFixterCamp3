from django.db import models
from django.contrib.auth.models import User


class Subject(models.Model):
	title = models.CharField(max_length=140)
	slug = models.SlugField(max_length=300)

class Course(models.Model):
	subject = models.ForeignKey(Subject, related_name='courses')
	alumni = models.ManyToManyField(User, related_name='courses')

from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import SubjectSerializer, CourseSerializer, CursoSerializer
from ..models import Subject, Course

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import detail_route

from .permissions import IsEnrolled

class SubjectViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Subject.objects.all()
	serializer_class = SubjectSerializer

class CourseViewSet(viewsets.ModelViewSet):
	queryset = Course.objects.all()
	# serializer_class = CourseSerializer
	serializer_class = CursoSerializer
	authentication_classes = (BasicAuthentication,)
	permission_classes = (IsAuthenticated,)

	@detail_route(methods=['get'],
		serializer_class=CursoSerializer,
		authentication_classes=[BasicAuthentication],
		permission_classes=[IsAuthenticated,IsEnrolled])
	def contents(self, request, *args, **kwargs):
		return self.retrieve(request, *args, **kwargs)

	@detail_route(methods=['post'], authentication_classes=[BasicAuthentication])
	def enroll(self, request, *args, **kwargs):
		course = self.get_object()
		course.alumni.add(request.user)
		return HttpResponse({'enrolled':True})




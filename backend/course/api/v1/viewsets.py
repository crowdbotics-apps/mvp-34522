from rest_framework import authentication
from course.models import Course
from .serializers import CourseSerializer
from rest_framework import viewsets


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Course.objects.all()

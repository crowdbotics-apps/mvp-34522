from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import CourseViewSet

router = DefaultRouter()
router.register("course", CourseViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

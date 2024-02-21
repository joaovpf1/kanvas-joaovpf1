from django.shortcuts import get_object_or_404
from courses.models import Course
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    RetrieveUpdateAPIView,
)
from courses.permissions import IsAdminOrReadOnly
from courses.serializers import CourseSerializer, CourseStudentAddSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication


# Create your views here.
class ListCreateCoursesApi(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = CourseSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            queryset = Course.objects.all()
            return queryset
        return Course.objects.filter(students=self.request.user)


class DetailCoursesApi(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = CourseSerializer
    lookup_url_kwarg = "course_id"

    def get_queryset(self):
        if self.request.user.is_superuser:
            queryset = Course.objects.all()
            return queryset
        return Course.objects.filter(students=self.request.user)

    def get_object(self):
        return get_object_or_404(Course, id=self.kwargs["course_id"])


class AddStudentCoursesApi(RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    queryset = Course.objects.all()
    serializer_class = CourseStudentAddSerializer
    lookup_url_kwarg = "course_id"

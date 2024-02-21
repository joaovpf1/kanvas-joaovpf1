from _core.permissions import IsAdminUser
from contents.models import Content
from contents.serializers import ContentSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from courses.models import Course
from students_courses.permissions import IsStudentContent
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound
from rest_framework import generics

# Create your views here.


class CreateContentApi(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = ContentSerializer

    def perform_create(self, serializer):
        course = Course.objects.filter(pk=self.kwargs["course_id"]).first()
        if not course:
            raise NotFound({"detail": "course not found."})
        serializer.save(course=course)


class DetailContentApi(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsStudentContent]
    serializer_class = ContentSerializer
    lookup_url_kwarg = "content_id"

    def get_object(self):
        try:
            Course.objects.get(id=self.kwargs["course_id"])
            content = Content.objects.get(id=self.kwargs["content_id"])
        except Course.DoesNotExist:
            raise NotFound({"detail": "course not found."})
        except Content.DoesNotExist:
            raise NotFound({"detail": "content not found."})
        self.check_object_permissions(self.request, content)
        return content

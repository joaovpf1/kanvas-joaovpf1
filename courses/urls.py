from django.urls import path

from courses.views import (
    DetailCoursesApi,
    ListCreateCoursesApi,
    AddStudentCoursesApi,
)


urlpatterns = [
    path("courses/", ListCreateCoursesApi.as_view()),
    path("courses/<course_id>/", DetailCoursesApi.as_view()),
    path("courses/<course_id>/students/", AddStudentCoursesApi.as_view()),
]

from django.urls import path

from contents.views import CreateContentApi, DetailContentApi


urlpatterns = [
    path("courses/<course_id>/contents/", CreateContentApi.as_view()),
    path("courses/<course_id>/contents/<content_id>/", DetailContentApi.as_view()),
]

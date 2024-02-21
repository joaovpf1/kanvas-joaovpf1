from rest_framework import serializers

from contents.models import Content


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ["id", "name", "content", "video_url"]
        extra_kwargs = {"course": {"read_only": True}}

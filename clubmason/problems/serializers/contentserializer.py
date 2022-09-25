from rest_framework import serializers
from taggit.serializers import TagListSerializerField, TaggitSerializer

from problems.models.content import Content

class ContentSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    class Meta:
        model = Content
        fields = '__all__'
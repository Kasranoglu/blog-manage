from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from api.auth.serializer import UserSerializer
from core.models import Post, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)


class PostSerializer(serializers.ModelSerializer):
    #tag = TagSerializer(many=True)
    author = UserSerializer()
    likes = UserSerializer(many=True)
    tags = SerializerMethodField()

    def get_tags(self, obj):
        return obj.tag.all().values("name")

    class Meta:
        model = Post
        fields = ('id', 'title', 'subtitle', 'slug', 'author', 'category', 'content', 'created_ad', 'updated_ad',
                  'status', 'image', 'tag', "tags", 'confirmation', 'likes')

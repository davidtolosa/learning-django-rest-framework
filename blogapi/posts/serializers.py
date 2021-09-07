from django.contrib.auth import models
from rest_framework import fields, serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'author', 'title', 'body', 'created_at')
        model = Post
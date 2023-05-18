from rest_framework import serializers
from .models import *


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'body', 'blog_image',  'status', 'user']

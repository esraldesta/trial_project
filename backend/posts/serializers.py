from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["title","body","likes"]

class PostCreateSerializer(serializers.ModelSerializer):
    author = serializers.CharField(read_only=True)
    class Meta:
        model = Post
        fields = ["title","body","author"]
    def create(self,request, *args, **kwargs):
        username = self.context.get("request").user
        user= User.objects.get(username=username)
        request["author"] = user
        return super().create(request, *args, **kwargs)
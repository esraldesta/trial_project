from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Post,Comment

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
    
class CommentSerializer(serializers.ModelSerializer):
    post = serializers.CharField(read_only=True)
    user = serializers.CharField(read_only=True)
    class Meta:
        model = Comment
        fields = ["comment","post","user"]


    def create(self,request,*args,**kwargs):
        username = self.context.get("request").user
        pk = self.context['view'].kwargs.get('pk')
        user= User.objects.get(username=username)
        post = Post.objects.get(id=pk)
        request["user"] = user
        request["post"] = post       
        return super().create(request,*args,**kwargs)
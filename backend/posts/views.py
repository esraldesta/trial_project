from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView,DestroyAPIView,ListAPIView
from .models import Post
from .serializers import PostCreateSerializer,PostSerializer

# Create your views here.
class CreatePostView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class  = PostCreateSerializer
    permission_classes = [IsAuthenticated]

class DeletePostView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class  = PostSerializer
    permission_classes = [IsAuthenticated]

class ListPostView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class  = PostSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view
@api_view()
def LikePostView(request,pk):
    print(request.user)
    post= Post.objects.filter(id=pk).first()
    if post.likes.filter(id=request.user.id):
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    
    return Response(PostSerializer(post).data)
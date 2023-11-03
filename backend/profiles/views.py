from django.shortcuts import render
from  rest_framework.generics import ListAPIView,RetrieveUpdateAPIView,RetrieveAPIView
from .serializers import ProfileListSerialzer,ProfileUpdateserialzer,ProfileRetrieveSerializer
from .models import Profile

# Create your views here.
class ProfileListView(ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileListSerialzer

class ProfileDetailView(RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileRetrieveSerializer

class ProfileUpdateView(RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileUpdateserialzer

from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User

@api_view()
def ProfileFollowView(request,pk):

    user = User.objects.filter(username=request.user).first()
    print(user)
    profile= Profile.objects.filter(id=pk).first()
    print(profile)
    print(user.id)
    userProfile = Profile.objects.filter(user__id=user.id).first()
    print(userProfile)
    if profile.follows.filter(id=userProfile.id):
        profile.follows.remove(userProfile)
    else:
        profile.follows.add(userProfile)
    return Response(ProfileRetrieveSerializer(profile).data)
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Profile

class ProfileListSerialzer(ModelSerializer):
    username = serializers.CharField(read_only=True,source="user.username")
    first_name = serializers.CharField(read_only=True,source="user.first_name")
    last_name = serializers.CharField(read_only=True,source="user.last_name")

    class Meta:
        model = Profile
        fields = ["id","created","user","username","first_name","last_name","image"]


class ProfileUpdateserialzer(ModelSerializer):
    first_name = serializers.CharField(source="user.first_name")
    last_name = serializers.CharField(source="user.last_name")
    class Meta:
        model = Profile
        fields = ["image","follows","first_name","last_name"]

    def update(self,request, *args, **kwargs):

        request.user.first_name = args[0]["user"]["first_name"]
        request.user.last_name = args[0]["user"]["last_name"]
        request.user.save()

        args[0].pop("user")
        if(args[0]["image"] == None):
            args[0].pop("image")
        return super().update(request,*args,**kwargs)

class ProfileRetrieveSerializer(ModelSerializer):
    username = serializers.CharField(read_only=True,source="user.username")
    first_name = serializers.CharField(read_only=True,source="user.first_name")
    last_name = serializers.CharField(read_only=True,source="user.last_name")
    class Meta:
        model = Profile
        fields = ["username","first_name","last_name","image","follows"]
from dataclasses import field
from rest_framework import serializers
from .models import User, UserImage, Test, Rasdata

class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('userid', 'userpassword', 'username', 'userbirth')


class ImageSerializer(serializers.ModelSerializer):

    userimage = serializers.ImageField(use_url=True)

    # userimage = Base64ImageField(max_length = None, use_url=True, required=False)
    
    class Meta:
        model = UserImage
        fields = ('user','userimage', 'plantname')


class RaspberrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Rasdata
        fields = ('temp', 'humid', 'soil_hum','light', 'date')

from .models import Plantmanage

class WaterDataSerializer(serializers.ModelSerializer): ##바뀐점!!!
    class Meta:
        model = Plantmanage
        fields = ('plant', 'waterdate')

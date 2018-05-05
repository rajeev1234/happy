
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Newsletter,News,Fileupload,htmlupload,newshtmlupload


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')

    # def create(self, validated_data):
    #     user=User.objects.create_user(**validated_data)
    #     return user


class newsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Newsletter
        fields = ('email',)

class headingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
            model = News
            fields = ('heading',)

class uploadSerializer(serializers.HyperlinkedModelSerializer):
    file = serializers.FileField( required=False,read_only=False,)
    class Meta:
        model = Fileupload
        fields = ('file',)

class htmlSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = htmlupload
        fields = ('file',)

class newshtmlSerializer(serializers.HyperlinkedModelSerializer):
    file = serializers.FileField(required=False, read_only=False, )
    class Meta:
        model = newshtmlupload
        fields = ('file',)
        #
        # def get_ip(request):
        #     try:
        #         x_forward = request.META.get("HTTP_X_FORWARDED_FOR")
        #         if x_forward:
        #             ip = x_forward.split(",")[0]
        #         else:
        #             ip = request.META.get("REMOTE_ADDR")
        #     except:
        #         ip = ""
        #     return ip


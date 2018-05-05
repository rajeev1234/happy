
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from .serializers import UserSerializer,newsSerializer,headingSerializer,uploadSerializer,htmlSerializer,newshtmlSerializer
from .forms import JoinForm
from .models import Newsletter,News,Fileupload,htmlupload,newshtmlupload
from django.shortcuts import render, HttpResponseRedirect
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.decorators import api_view


import requests

def demo(request):
    return render(request,'demo.html')

def geo(request):
    ip_address = request.META.get('HTTP_X_FORWARDED_FOR', '')
    response = requests.get('http://freegeoip.net/json/%s' % ip_address)
    geodata = response.json()
    return render(request, 'geo.html', {
        'ip': geodata['ip'],
        'country': geodata['country_name'],
        'latitude': geodata['latitude'],
        'longitude': geodata['longitude'],
        'api_key': 'AIzaSyCb-xgwWOdV86BgHvm8YzzjCssYwH6htJo'  # Don't do this! This is just an example. Secure your keys properly.
    })




class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)


# class CustomObtainAuthToken(ObtainAuthToken):
#     def post(self, request, *args, **kwargs):
#         response = super(CustomObtainAuthToken,self).post(request,*args ,**kwargs)
#         token = Token.objects.get(key=response.data['token'])
#         user = User.objects.get(id=token.user_id)
#         serializer = UserSerializer(user , many=False)
#         print(token.key)
#         return Response({'token': token.key, 'user' : serializer.data})

def get_ip(request):
    try:
        x_forward = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forward:
            ip = x_forward.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR")
    except:
        ip = ""
    return ip


def home(request):
    form = JoinForm(request.POST or None)
    if form.is_valid():
        new_join = form.save(commit=False)
        email = form.cleaned_data['email']
        new_join_old, created = Newsletter.objects.get_or_create(email=email)
        new_join_old.ip_address = get_ip(request)
        new_join_old.save()

        return HttpResponseRedirect("/%s" % ("thankyou"))

    context = {"form": form}
    template = "home.html"
    return render(request, template, context)





class NewsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Newsletter.objects.all()
    serializer_class = newsSerializer

class headingViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = headingSerializer

class uploadViewSet(viewsets.ModelViewSet):
    queryset = Fileupload.objects.all()
    serializer_class = uploadSerializer

class htmlViewSet(viewsets.ModelViewSet):
    queryset = htmlupload.objects.all()
    serializer_class = htmlSerializer

class newshtmlViewSet(viewsets.ModelViewSet):
    queryset = newshtmlupload.objects.all()
    serializer_class = newshtmlSerializer

    # #
    # @api_view(['GET', 'POST'])
    # def get_ip(self, request):
    #     ip = self.get_object()
    #     serializer = newsSerializer(data=request.data)
    #     if serializer.is_valid():
    #         try:
    #             x_forward = request.META.get("HTTP_X_FORWARDED_FOR")
    #             if x_forward:
    #                 ip = x_forward.split(",")[0]
    #             else:
    #                 ip = request.META.get("REMOTE_ADDR")
    #         except:
    #             ip = ""
    #         return ip
    #
    #     else:
    #         return Response("noip")













from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
# Create your views here.
class RegisterUsernameCountAPIView(APIView):
    """
    获取用户名的个数
    GET:  /users/usernames/(?P<username>\w{5,20})/count/
    """
    def get(self,username,count):
        count = User.objects.filter(username = username).count()
        context={
            "count":count,
            "username":username,
        }
        return Response(context)





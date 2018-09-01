from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django_redis import get_redis_connection
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView

from libs.captcha.captcha import captcha


class RegisterImagecodeView(APIView):
    """GET  <<(?P<image_code_id>.+)/"""
    def get(self,request,image_code_id):
        # 创建图片和验证码
        text, image = captcha.generate_captcha()
        # 通过redis进行保存验证码
        redis_conn = get_redis_connection('code')
        redis_conn.setex('img_%s' % image_code_id, 60, text)
        # 将图片返回
        # 注意,图片是二进制,我们通过HttpResponse返回
        return HttpResponse(image, content_type='image/jpeg')

class ResgiserSmsCodeview(GenericAPIView):
    """
      获取短信验证码
      GET /verifications/smscodes/(?P<mobile>1[345789]\d{9})/?text=xxxx&image_code_id=xxxx
      获取短信验证码,首先需要校验 验证码

      思路:
      创建序列化器,定义text 和 image_code_id
      redis 判断该用户是否频繁获取
      生成短信验证码
      redis增加记录
      发送短信
      返回响应
      """



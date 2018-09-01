from django.conf.urls import url

from verifications import views


urlpatterns = [
    # verifications/imagecodes/(?P<image_code_id>.+)/
    url(r'^imagecodes/(?P<image_code_id>.+)/$', views.RegisterImagecodeView.as_view(), name='imagecode'),

]

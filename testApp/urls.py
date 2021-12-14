from django.conf.urls import url
# from rest_framework import routers

from testApp.views import *

# router = routers.DefaultRouter()

urlpatterns = [
    url(r'^/postdemo', PostDemoViews, name='postdemo')
]

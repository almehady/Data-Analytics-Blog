from django.urls import path
from . import views
from .views import *
from django.urls import path, re_path, include
from rest_framework import routers
# router = routers.DefaultRouter()
# router.register(r'api/blog/', BlogViewSet, basename='blog')

urlpatterns = [
    path("", views.index, name="home"),
    path("about/", views.about, name="about_us"),
    path('api/v1/blog/', BlogViewSet.as_view({'get': 'list'}), name='bloglist'),
    path("blog/", views.blog, name="blog"),
]
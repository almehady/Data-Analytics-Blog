from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path("", views.index, name="home"),
    path("about/", views.about, name="about_us"),
    path('v1/blog/', BlogViewSet.as_view({'get': 'list'}), name='bloglist')
]
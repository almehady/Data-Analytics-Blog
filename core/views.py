from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .serializers import *
from rest_framework import permissions, renderers, viewsets, generics, mixins
# Create your views here.

def index(request):
    return HttpResponse("Welcome to our data blog")

def about(request):
    return HttpResponse("this is about page")


class BlogViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    All blog viewset
    * Methods : GET and POST
    * Only authenticated user will get access to his/her blog post only
    '''
    queryset = Blog.objects.filter(status='P')
    serializer_class = BlogSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    http_method_names = ['get']

def blog(request):
    blogs = Blog.objects.all().filter(status='P')
    print(blogs)
    my_company = 'ADN Diginet'

    context = {
        'blogs': blogs,
        'my_company': my_company
    }
    return render (request, 'index.html', context)
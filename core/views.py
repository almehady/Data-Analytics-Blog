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


class BlogViewSet(mixins.CreateModelMixin,
                                mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                viewsets.GenericViewSet):
    '''
    All blog viewset
    * Methods : GET and POST
    * Only authenticated user will get access to his/her blog post only
    '''
    queryset = Blog.objects.filter(status='P')
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
    def get_queryset(self, *args, **kwargs):
        if self.action == 'list':
            print('is user authenticated', self.request.user.is_authenticated)
            print('requested user', self.request.user)
            if self.request.user.is_authenticated:
                return self.queryset.filter(user=self.request.user)
        return self.queryset


def blog(request):
    blogs = Blog.objects.all().filter(status='P')
    print(blogs)
    my_company = 'ADN Diginet'

    context = {
        'blogs': blogs,
        'my_company': my_company
    }
    return render (request, 'index.html', context)
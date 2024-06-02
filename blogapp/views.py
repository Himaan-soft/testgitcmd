from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Blog 
from .serializers import BlogSerializers

# Create your views here.

@api_view(['GET'])
def blog_list(request):
    blogs = Blog.objects.all()
    serializers =  BlogSerializers(blogs, many=True)

    return Response(serializers.data)

def hello_world(request):
    return HttpResponse('Hello World, Laxmi Kumar Yadav !!')

def main_page(request):
<<<<<<< HEAD
    return render(request, 'main.html', {'name' : 'Laxmi Narayan yadav'})


=======
    return render(request, 'main.html', {'name' : 'laxmi yadav'})
>>>>>>> 7fe7abd (views: updated HttpResponse)

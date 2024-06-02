
<!-- INSTALL DJANGO REST FRAMEWORK  -->

<!-- install django REST framework -->
pip install djangorestframework

<!-- setting.py -->
INSTALLED_APPS = [
    ...
    'rest_framework',
]

<!-- views.py -->

from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET'])
def api_data(request):
    api_urls = {
        'list' : '/task-list',
        'Detail' : '/task-detail/<str:pk>/',
    } 
    return Response(api_urls)

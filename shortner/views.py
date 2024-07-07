from django.shortcuts import render ,redirect
import uuid #uniq
from .models import Url
from django.http import HttpResponse
from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response
from .serializers import UrlSerializer


# Create your views here.
def index(request):
    return render(request, 'index.html')

def create(request):
    if request.method == 'POST':
        link = request.POST['link']
        uid = str(uuid.uuid4())[:5] #generate id of 5 length
        new_url = Url(link=link,uuid=uid) 
        new_url.save() # to save an object
        return HttpResponse(uid)
    
def go(request, pk):
    url_details = Url.objects.get(uuid=pk)
    return redirect(url_details.link)

@api_view(['GET'])
def allUrls(request):
    urls = Url.objects.all()
    serializer = UrlSerializer(urls,many=True) #to convert to json | qs== query Set
    return Response({"urls":serializer.data })

@api_view(['POST'])
def createApi(request):
    
    serializer = UrlSerializer(data=request.data) #to convert to json
    
    if serializer.is_valid():  # Check if the data is valid
        link = serializer.validated_data.get('link')
        uid = str(uuid.uuid4())[:5] #generate id of 5 length
        new_url = Url(link=link,uuid=uid) 
        new_url.save() # to save an object
        res = UrlSerializer(new_url , many=False) #many = we created one product
        return Response({"urls":res.data})
    else:
        return Response(serializer.errors,status=400)
    
    
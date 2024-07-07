# serializers is used to send data as json
from rest_framework import serializers
from .models import Url
   
class UrlSerializer(serializers.ModelSerializer):
   
    
    class Meta: #to declare which data i wanna send
        model = Url
        fields = '__all__' # return all
        #fields = ('name','price','brand')


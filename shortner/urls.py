from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('<str:pk>/', views.go, name='go'),
    ###########################################
    path('api/all', views.allUrls, name='allUrls'),
    path('api/create', views.createApi, name='createApi'),
    
]
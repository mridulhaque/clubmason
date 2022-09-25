import imp
from django.urls import path
from .views import ContentsAPI

urlpatterns = [
    path('content/<int:pk>/', ContentsAPI.as_view(), name = 'contents_api_pk'),
    path('content/',ContentsAPI.as_view(), name = 'contents_api'),
]

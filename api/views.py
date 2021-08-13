import os
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from utils import effects, imageRequests

# Create your views here.
@api_view(['GET'])
def grayscale(request):
    unsplashUrl = request.GET.get('img')

    imgPath = imageRequests.downloadImageFromURL(unsplashUrl)
    newPath = effects.grayscale(imgPath)

    #do this in reality
    s3Url = imageRequests.uploadImageToS3(newPath)

    return Response({"message": "here's ye grayscale", "url": s3Url})

from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import ContactSerializer

# Create your views here.
def index (request):
    return render(request,"index.html")


def resume(request):
    return render(request,"resume.html")


@api_view(['POST'])
def contact_api(request):
    serializer = ContactSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Message sent successfully!"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



def contact(request):
    return render(request,"contact.html")


def project(request):
    return render(request,"project.html")
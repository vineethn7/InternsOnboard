from django.shortcuts import render, redirect
from .models import internshipPost
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import internshipPostSerializer

def home(request):
    internships = internshipPost.objects.all()
    return render(request,'InternsOnboardMain/home.html',{'internships':internships})

def about(request):
    return render(request,'InternsOnboardMain/about.html')

class internshipPostList(APIView):
    def get(self,request):
        internships = internshipPost.objects.all()
        serializer = internshipPostSerializer(internships, many=True)
        return Response(serializer.data)
    def post(self):
        pass

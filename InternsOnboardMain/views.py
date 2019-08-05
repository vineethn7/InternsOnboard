from django.shortcuts import render, redirect
from .models import internshipPost
from .forms import internshipPostForm
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import internshipPostSerializer

def home(request):
    if request.method == 'POST':
        form = internshipPostForm(request.POST)
        if form.is_valid():
            form.save()
            CompanyName = form.cleaned_data.get('company_name')
            messages.success(request, 'Internship {} Posted successfully!'.format(CompanyName))
            return redirect('InternsOnboard-About')
    else:
        form =internshipPostForm()
    return render(request,'InternsOnboardMain/home.html',{'form': form})

def about(request):
    return render(request,'InternsOnboardMain/about.html')

class internshipPostList(APIView):
    def get(self,request):
        internships = internshipPost.objects.all()
        serializer = internshipPostSerializer(internships, many=True)
        return Response(serializer.data)
    def post(self):
        pass

<<<<<<< HEAD
from django.shortcuts import render, redirect
from django.contrib import messages
from InternsOnboardMain.models import internshipPost

def apply(request):
    internships = internshipPost.objects.all()
    return render(request,'studentPortal/apply.html',{'internships':internships})
=======
from django.shortcuts import render

# Create your views here.
>>>>>>> master

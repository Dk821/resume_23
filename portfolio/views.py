from django.shortcuts import render
from .models import *




def home(request):
    profile = Profile.objects.all()
    works= Work.objects.all()
    certificate = Certificate.objects.all()
    context ={
        'profile':profile,'work':works ,
        'certificate':certificate
    }
    return render(request,"about.html",context)


def Projects(request):
    project = Project.objects.all()
    profile = Profile.objects.all()
    
    context ={'profile':profile, 
             'project':project }
    return render(request,"project.html",context)


def Resume(request):
    skills = Skills.objects.all()
    education = Education.objects.all()
    profile = Profile.objects.all()
    context ={'profile':profile,
              'education':education,
              'skills':skills,
              }
    return render(request,"Resume.html",context)



def contact(request):
    profile = Profile.objects.all()
    context ={'profile':profile,}
    return render(request,"contact.html",context)


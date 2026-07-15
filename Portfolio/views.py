from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Skill, Project, Experience, ContactMessage, Category

def home(request):
    if request.method == "POST":
        # Capture the data from the HTML form
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Save it to the database
        ContactMessage.objects.create(name=name, email=email, message=message)
        
        # We use redirect to clear the form so refreshing doesn't resubmit
        return redirect('home')

    skills = Skill.objects.all()
    projects = Project.objects.all().order_by('-id')
    experiences = Experience.objects.all().order_by('-id')
    categories = Category.objects.all()
    
    total_projects = projects.count()

    total_hackathons = projects.filter(category='HACK').count()

    context = {
        'skills': skills,
        'projects': projects,
        'experiences': experiences,
        'total_projects': total_projects,
        'total_hackathons': total_hackathons,
        'categories': categories,
    }
    return render(request, 'index.html', context)
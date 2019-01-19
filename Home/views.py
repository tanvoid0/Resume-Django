from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import *


# Create your views here.
def test(request):
    ar = ['a', 'b', 'c', 'D', 'e']
    context = {
        "ar" : ar
    }
    return render(request, "test.html", context)


def index(request):
    info = Info.objects.all()[:1].get()
    socials = Social.objects.all()
    hobbies = Hobby.objects.all()
    skills = Skill.objects.all()
    educations = Education.objects.all()
    trainings = Training.objects.all()
    works = Work.objects.all()
    testimonials = Testimonial.objects.all()
    facts = Fact.objects.all()
    projects = Project.objects.all()
    context = {
        "info" : info,
        "socials" : socials,
        "hobbies" : hobbies,
        "skills" : skills,
        "educations" : educations,
        "trainings" : trainings,
        "works" : works,
        "testimonials" : testimonials,
        "facts": facts,
        "projects" : projects
    }
    return render(request, "index.html", context)
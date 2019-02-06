from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from portfolio.models import Project, Project_Category


def test(request):
    projects = Project.objects.all()
    tags = Project_Category.objects.all
    context = {
        "projects" : projects,
        "tags" : tags
    }
    return render(request, "portfolio.html", context)
    # return HttpResponse("Hello world")
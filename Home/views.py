from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import Context
from django.template.loader import get_template
from django.views.generic.base import View

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


def cv(request):
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
        "info": info,
        "socials": socials,
        "hobbies": hobbies,
        "skills": skills,
        "educations": educations,
        "trainings": trainings,
        "works": works,
        "testimonials": testimonials,
        "facts": facts,
        "projects": projects,
    }
    return render(request, "cv.html", context)


def GeneratePdf(request):
    # def get(self, request, *args, **kwargs):
    #     # getting the template
    #     info = Info.objects.all()[:1].get()
    #     socials = Social.objects.all()
    #     hobbies = Hobby.objects.all()
    #     skills = Skill.objects.all()
    #     educations = Education.objects.all()
    #     trainings = Training.objects.all()
    #     works = Work.objects.all()
    #     testimonials = Testimonial.objects.all()
    #     facts = Fact.objects.all()
    #     projects = Project.objects.all()
    #     context = {
    #         "info": info,
    #         "socials": socials,
    #         "hobbies": hobbies,
    #         "skills": skills,
    #         "educations": educations,
    #         "trainings": trainings,
    #         "works": works,
    #         "testimonials": testimonials,
    #         "facts": facts,
    #         "projects": projects,
    #     }
    #     pdf = render_to_pdf('invoice.html', context)
    #
    #     # rendering the template
    #     return HttpResponse(pdf, content_type='application/pdf')
    template = get_template("test.html")
    # context = Context({'pagesize': 'A4'})
    context = {
        'pagesize': 'A4'
    }
    html = template.render(context)
    result = StringIO.StringIO()
    pdf = pisa.pisaDocument(StringIO.StringIO(html), dest=result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    else:
        return HttpResponse('Errors')

def weditor(request):
    return render(request, "weditor.html")

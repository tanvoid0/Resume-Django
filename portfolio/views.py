from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def test(request):
    ar = ['a', 'b', 'c', 'D', 'e']
    context = {
        "ar" : ar
    }
    return render(request, "portfolio.html", context)
    # return HttpResponse("Hello world")
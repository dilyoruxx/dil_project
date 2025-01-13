from django.shortcuts import render
from django.http import HttpResponse

from apps.base.models import About

# Create your views here.
# def index(request):
#     return HttpResponse("<i>hello world</i>")

# def about(request):
#     text = "меня зовут дилёр я изучаю django"
#     return HttpResponse(text)

def index(request):
    return render(request, "index.html")

def about(request):
    # about = About.objects.latest('id')
    return render(request, 'about.html', locals())
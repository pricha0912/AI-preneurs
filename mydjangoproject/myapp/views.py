from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.views.generic import TemplateView

from django.http import HttpResponse


# Create your views here.

def index(request):
    #return HttpResponse("Hello, this is my first django project, good to do.")
    return render(request,"index.html")

def home(request):
    contecxt = {}
    if request.method == "POST":
        name = request.POST['myvalue']
        fs= FileSystemStorage()
        fname = fs.save(name.name,name)
        context['url']  = fs.url(name)



    #return HttpResponse("Hello, this is my first django project, good to do.")
    text = "this is my text"
    a = 35
    b = 10
    result = a * b
    content = {
        't1' : text,
        'cal' : result
    }
    return render(request, "home.html", { 'd1' : content, 'context' : [' hello', 'world', 'richa'],'getvalue' : name})




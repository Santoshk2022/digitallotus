
from django.shortcuts import render, HttpResponse
from hello import views 
# Create your views here.
def index(request):
    context= {
        'variable' : 'Welcome to digital world'
    }
    # return HttpResponse ("<h1>Hello World</h1>")
    return render(request, 'index.html', context)

def about(request):
    return HttpResponse ("<h1>Pushpa Is Best Movie</h1>")

def contact(request):
    return HttpResponse ("<h1>9075557158</h1>")
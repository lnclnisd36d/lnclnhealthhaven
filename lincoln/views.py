from django.shortcuts import render


# Create your views here.
def about(request):
    return render(request, 'about.html')
def home(request):
    return render(request, 'index.html')
def blog(request):
    return render(request, 'blog.html')
def contact(request):
    return render(request, 'contact.html')

def departments(request):
    return render(request, 'departments.html')

def doctor(request):
    return render(request, 'doctor.html')
def readme1(request):
    return render(request, 'readme1.html')
def readmore(request):
    return render(request, 'readmore.html')
def readmore1(request):
    return render(request, 'readmore1.html')
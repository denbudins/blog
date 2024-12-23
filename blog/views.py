from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'blog/home-page.html')

def posts(request):
    pass

def post_detail(request, slug):
    pass
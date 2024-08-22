from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'webpages/index.html')
def about(request):
    return render(request, 'webpages/about.html')
def contact(request):
    return render(request, 'webpages/contact.html')
def blog(request):
    return render(request, 'webpages/blog.html')
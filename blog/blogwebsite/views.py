from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2023'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2023'
    },
    {        
        'author': 'John Smith',
        'title': 'Blog Post 3',
        'content': 'Third post content',
        'date_posted': 'August 29, 2023'
    }
]

# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blogwebsite/home.html', context)

def about(request):
    return render(request, 'blogwebsite/about.html', {'title': 'About'})
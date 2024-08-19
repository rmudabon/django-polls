from django.shortcuts import render

# Create your views here.

posts = [
    {
        'author': 'Marco Dabon',
        'title': 'My First Post',
        'content': 'First Post!',
        'date_posted': 'August 10, 2024'
    },
    {
        'author': 'Marco Dabon',
        'title': 'My Second Post',
        'content': 'Second Post!',
        'date_posted': 'August 11, 2024'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
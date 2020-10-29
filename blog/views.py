from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Anh Vu',
        'title': 'Introduction to React Native',
        'content': 'React Native is a mobile cross-platform library',
        'date_posted': 'October 28, 2020'
    },
    {
        'author': 'Jane Doe',
        'title': 'Advanced React Native',
        'content': 'React Native can run the app in 60fps',
        'date_posted': 'October 28, 2020'
    },
    {
        'author': 'John Smith',
        'title': 'Introduction to React',
        'content': 'React is made by Facebook',
        'date_posted': 'October 28, 2020'
    }
]
def home(request):
    context = {
        'posts': posts,
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
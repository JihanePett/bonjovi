from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'home/index.html')


def bjcards(request):
    return render(request, 'home/bjcards.html')


def music(request):
    return render(request, 'home/music.html')


def tours(request):
    return render(request, 'home/tours.html')

from django.shortcuts import render

# Create your views here.
""" A view that renders the shopping bag contents page """


def index(request):
    return render(request, 'bag/bag.html')

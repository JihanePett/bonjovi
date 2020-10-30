from django.shortcuts import render

# Create your views here.
""" A view that renders the shopping bag contents page """


def view_bag(request):
    return render(request, 'bag/bag.html')

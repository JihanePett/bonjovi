from django.shortcuts import render

# Create your views here.


def profile(request):
    """ To display the user profile """
    template = 'profiles/profiles.html'
    context = {}
    return render(request, template, context)

from django.shortcuts import render


def index(request):
    return render(request, 'core/index.html')


def inscription(request):
    return render(request, 'core/inscription.html')


def parent(request):
    return render(request, 'core/parent.html')


def connexio(request):

    return render(request, 'core/connexio.html')

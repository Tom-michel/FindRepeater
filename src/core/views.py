from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'core/index.html')
def inscription(request):
    return render(request,'core/inscription.html')
def parent(request):
    return render(request, 'core/parent.html')
def connexio(request):
    return render(request, 'core/connexio.html')
def test(request):
    return render(request, 'core/test.html')
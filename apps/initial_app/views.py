from django.shortcuts import render

def index(request):
    return render(request, 'initial_app/index.html')
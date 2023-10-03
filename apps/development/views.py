from django.shortcuts import render

def index(request):
    return render(request, 'development/index.html', {'title':'home'})
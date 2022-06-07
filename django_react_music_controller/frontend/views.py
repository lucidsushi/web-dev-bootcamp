from django.shortcuts import render

# Create your views here.
def index(request, *args, **kwargs):
    # looks in "templates" folder?
    return render(request, 'frontend/index.html')

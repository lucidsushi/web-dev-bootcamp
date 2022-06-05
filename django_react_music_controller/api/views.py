from django.shortcuts import render
from django.http import HttpResponse

# Create your views (endpoints) here.
# Django server auto reloads the code when you save views
def main(request):
    # return render(request, 'main.html')
    return HttpResponse("<h1>Hello, world.</h1>")

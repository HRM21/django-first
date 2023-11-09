# contains functions and classes that handles what data is being displayed on the HTML pages
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'pages/home.html', {})


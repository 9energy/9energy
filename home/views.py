from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        "title": "9 Energy Solar"
    }
    return render(request, "home/home.html", context)
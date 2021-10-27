from django.shortcuts import render

from energysolar.settings import EMAIL_RECEIVER, FACEBOOK, LOCATION_ADDRESS, LOCATION_LINK

# Create your views here.
def home(request):
    context = {
        "title": "9 Energy Solar",
        "emailReceiver": EMAIL_RECEIVER,
        "locationAddress": LOCATION_ADDRESS,
        "locationLink": LOCATION_LINK,
        "facebook": FACEBOOK,
    }
    return render(request, "home/home.html", context)
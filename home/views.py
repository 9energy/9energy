from django.shortcuts import render
from energysolar.settings import EMAIL_RECEIVER, FACEBOOK, LINKEDIN, LOCATION_ADDRESS, LOCATION_LINK, TWITTER
import os

# Create your views here.
def home(request):
    context = {
        "title": "9 Energy Solar",
        "emailReceiver": EMAIL_RECEIVER,
        "locationAddress": LOCATION_ADDRESS,
        "locationLink": LOCATION_LINK,
        "facebook": FACEBOOK,
        "linkedin": LINKEDIN,
        "twitter": TWITTER,
        "allProds": os.listdir("static/images/products")
    }
    return render(request, "home/home.html", context)
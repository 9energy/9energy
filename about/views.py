from django.shortcuts import render

from energysolar.settings import EMAIL_RECEIVER, LINKEDIN, LOCATION_ADDRESS, LOCATION_LINK, FACEBOOK, TWITTER

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
    }
    return render(request, "about/home.html", context)
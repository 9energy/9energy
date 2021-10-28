from django.shortcuts import render, HttpResponse
import json, os
from energysolar.settings import EMAIL_RECEIVER, LINKEDIN, LOCATION_LINK, LOCATION_ADDRESS, FACEBOOK, TWITTER, YOUTUBE

class GalleryRetriever():    
    def __init__(self):
        self.PATH = "static/images/gallery"

    def allSections(self):
        return os.listdir(self.PATH)

    def getImages(self, section):
        section = os.path.join(self.PATH, section)
        return os.listdir(section)

    def getImagesGroupBySection(self):
        imagesBySection = {}
        for section in self.allSections():
            imagesBySection[section] = self.getImages(section)
        return imagesBySection


# Create your views here.

def home(request):
    obj = GalleryRetriever()

    context = {
        "title": "9 Energy Solar",
        "gallery": obj.getImagesGroupBySection(),
        "emailReceiver": EMAIL_RECEIVER,
        "locationAddress": LOCATION_ADDRESS,
        "locationLink": LOCATION_LINK,
        "facebook": FACEBOOK,
        "linkedin": LINKEDIN,
        "twitter": TWITTER,
        "youtube": YOUTUBE
    }
    return render(request, "gallery/home.html", context)
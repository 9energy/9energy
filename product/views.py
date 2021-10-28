from django.shortcuts import render, HttpResponse
from energysolar.settings import EMAIL_RECEIVER, LINKEDIN, LOCATION_ADDRESS, LOCATION_LINK, FACEBOOK, TWITTER, YOUTUBE
import os
import json

class ProductRetreiver():    
    def __init__(self):
        self.PATH = "static/images/products"

    def getAllProducts(self):
        return os.listdir(self.PATH)

    def getProductImages(self, product):
        product = os.path.join(self.PATH, product)
        images = []
        for img in os.listdir(product):
            if img == "data.json":
                continue    
            loc = os.path.join(product, img)
            images.append(loc)
        return images

    def getImagesGroupByProduct(self):
        allProds = self.getAllProducts()
        allImages = {}

        for prod in allProds:
            allImages[prod] = []

            for img in self.getProductImages(prod):
                allImages[prod].append(img)

        return allImages

    def getProductDetails(self, product):
        loc = os.path.join(self.PATH, product, "data.json")
        with open(loc, 'r') as f:
            data = f.read()
        data = json.loads(data)
        return data

# Create your views here.

def home(request, productName):
    obj = ProductRetreiver()
    data = obj.getProductDetails(productName)

    context = {
        "title": "9 Energy Solar",
        "product": productName,
        "images": obj.getProductImages(productName),
        "details": data["details"],
        "oldPrice": data["oldPrice"],
        "newPrice": data["newPrice"],
        "emailReceiver": EMAIL_RECEIVER,
        "locationAddress": LOCATION_ADDRESS,
        "locationLink": LOCATION_LINK,
        "facebook": FACEBOOK,
        "twitter": TWITTER,
        "linkedin": LINKEDIN,
        "youtube": YOUTUBE
    }
    
    return render(request, "product/home.html", context)

def allProducts(request):
    if request.method == "POST":
        obj = ProductRetreiver()
        return HttpResponse(json.dumps({"products": obj.getAllProducts()}))
    else:
        return HttpResponse(json.dumps({"status": "failed"}))
PATH = "static/images/gallery"
import os
import json

from django.http.response import HttpResponse

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
        
obj = GalleryRetriever()
print(obj.getImagesGroupBySection())
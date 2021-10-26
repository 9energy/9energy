from django.shortcuts import render

# Create your views here.
def home(request):
    galleryImages = list()
    lmt = 1
    gallery = {
        "BATTERY LESS SOLAR INVERTER 1 KVA": [
                "/static/images/gallery/pic1.png",
                "/static/images/gallery/pic2.png",
                "/static/images/gallery/pic3.png",
                "/static/images/gallery/pic4.png",
                "/static/images/gallery/pic5.png",
            ],
        "LEAD ACID TALL TUBULAR BATTERY": [
                "/static/images/gallery/pic6.png",
                "/static/images/gallery/pic7.png",
                "/static/images/gallery/pic8.png",
                "/static/images/gallery/pic9.png",
                "/static/images/gallery/pic10.png",
            ],
        "MPPT SOLAR PCU 1KVA-12V": [
                "/static/images/gallery/pic11.png",
                "/static/images/gallery/pic12.png",
                "/static/images/gallery/pic13.png",
                "/static/images/gallery/pic14.png",
                "/static/images/gallery/pic15.png",
            ],
        "MPPT SOLAR PCU 5KVA-48-96V": [
                "/static/images/gallery/pic16.png",
                "/static/images/gallery/pic17.png",
                "/static/images/gallery/pic18.png",
                "/static/images/gallery/pic19.png",
                "/static/images/gallery/pic20.png",
            ],
        "PWM SOLAR PCU 3KVA-48V": [
                "/static/images/gallery/pic21.png",
                "/static/images/gallery/pic22.png",
                "/static/images/gallery/pic23.png",
                "/static/images/gallery/pic24.png",
                "/static/images/gallery/pic25.png",
            ],
        "PWM SOLAR PCU 2515-24V": [
                "/static/images/gallery/pic26.png",
                "/static/images/gallery/pic27.png",
                "/static/images/gallery/pic28.png",
                "/static/images/gallery/pic29.png",
                "/static/images/gallery/pic30.png",
            ],
        "PWM SOLAR PCU 1215-12V": [
                "/static/images/gallery/pic31.png",
                "/static/images/gallery/pic32.png",
                "/static/images/gallery/pic33.png",
                "/static/images/gallery/pic34.png",
                "/static/images/gallery/pic35.png",
            ],
        "MPPT 125O": [
                "/static/images/gallery/pic36.png",
            ],
        "LFP MPPT 125O": [
                "/static/images/gallery/pic37.png",
            ],
            
    }
 
    context = {
        "title": "9 Energy Solar",
        "gallery": gallery,
    }
    return render(request, "gallery/home.html", context)
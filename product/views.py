from django.shortcuts import render

# Create your views here.

products = {
    "BATTERY LESS SOLAR INVERTER 1 KVA": {
        "img": [
            "/static/images/gallery/pic1.png",
            "/static/images/gallery/pic2.png",
            "/static/images/gallery/pic3.png",
            "/static/images/gallery/pic4.png",
            "/static/images/gallery/pic5.png",
        ],
        "oldPrice": "15215",
        "newPrice": "14200",
        "details": [
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic.", 
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic.",
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic.",    
        ]
    },
    "LEAD ACID TALL TUBULAR BATTERY": {
        "img": [
            "/static/images/gallery/pic6.png",
            "/static/images/gallery/pic7.png",
            "/static/images/gallery/pic8.png",
            "/static/images/gallery/pic9.png",
            "/static/images/gallery/pic10.png",
        ],
        "oldPrice": "17408",
        "newPrice": "16400",
        "details": [
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic.", 
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic.",
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic.",    
        ]
    },
    "MPPT SOLAR PCU 1KVA-12V": {
        "img": [
            "/static/images/gallery/pic11.png",
            "/static/images/gallery/pic12.png",
            "/static/images/gallery/pic13.png",
            "/static/images/gallery/pic14.png",
            "/static/images/gallery/pic15.png",
        ],
        "oldPrice": "14180",
        "newPrice": "13100",
        "details": [
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic.", 
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic.",
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic.",    
        ]
    },
    "MPPT SOLAR PCU 5KVA-48-96V": {
        "img": [
            "/static/images/gallery/pic16.png",
            "/static/images/gallery/pic17.png",
            "/static/images/gallery/pic18.png",
            "/static/images/gallery/pic19.png",
            "/static/images/gallery/pic20.png",
        ],
        "oldPrice": "77594",
        "newPrice": "71000",
        "details": [
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic.", 
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic.",
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic.",    
        ]
    },
    "PWM SOLAR PCU 3KVA-48V": {
        "img": [
            "/static/images/gallery/pic21.png",
            "/static/images/gallery/pic22.png",
            "/static/images/gallery/pic23.png",
            "/static/images/gallery/pic24.png",
            "/static/images/gallery/pic25.png",
        ],
        "oldPrice": "30945",
        "newPrice": "28500",
        "details": [
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic.", 
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic.",
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic.",    
        ]
    },
    "PWM SOLAR PCU 2515-24V": {
        "img": [
            "/static/images/gallery/pic26.png",
            "/static/images/gallery/pic27.png",
            "/static/images/gallery/pic28.png",
            "/static/images/gallery/pic29.png",
            "/static/images/gallery/pic30.png",
        ],
        "oldPrice": "20717",
        "newPrice": "18700",
        "details": [
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic.", 
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic.",
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic.",    
        ]
    },
    "PWM SOLAR PCU 1215-12V": {
        "img": [
            "/static/images/gallery/pic31.png",
            "/static/images/gallery/pic32.png",
            "/static/images/gallery/pic33.png",
            "/static/images/gallery/pic34.png",
            "/static/images/gallery/pic35.png",
        ],
        "oldPrice": "7724",
        "newPrice": "7000",
        "details": [
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic.", 
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic.",
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic.",    
        ]
    },
    "MPPT 125O": {
        "img": [
            "/static/images/gallery/pic36.png",
        ],
        "oldPrice": "7724",
        "newPrice": "7000",
        "details": [
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic.", 
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic.",
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic.",    
        ]
    },
    "LFP MPPT 125O": {
        "img": [
            "/static/images/gallery/pic37.png",
        ],
        "oldPrice": "7724",
        "newPrice": "7000",
        "details": [
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic.", 
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic.",
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic.",    
        ]
    }
}


def home(request, productName):
    prodData = products[productName]

    context = {
        "title": "9 Energy Solar",
        "product": productName,
        "images": prodData["img"],
        "details": prodData["details"],
        "oldPrice": prodData["oldPrice"],
        "newPrice": prodData["newPrice"],
    }
    return render(request, "product/home.html", context)

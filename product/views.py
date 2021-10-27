from django.shortcuts import render

from energysolar.settings import EMAIL_RECEIVER, LOCATION_ADDRESS, LOCATION_LINK, FACEBOOK

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
            "No Battery Required",
            "BLS Solar System will work on the solar as well as Grid",
            "Precise auto thermal management and protection",
            "Advance and reliable software to incorporate and interface",
            "Maximum utilization of Solar energy",
            "Cuts down grid electricity consumption", 
            "maximum grid power saving",
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
            "99.97% - 99.99% Pure lead • Full capacity/True AH output",   
            "100% factory charged",   
            "100% factory charged battery",   
            "Hi-efficency grid design mode of Selenium/low Antimony alloy with grain refiners for low water loss ,least corrosion long life",   
            "Low self discharge",   
            "Heavy duty terminals",   
            "Ceramic water level management system with micro porous vent plugs for least environmental pollution & less topping up",   
            "Rugged anti-corrasive addictive-for longer battery life",   
            "Computerized formation -for uniform quality and peak performance Container made of PP Co-polymer for strength & robustnessi",   
            "More ribs on container for better strength • Paper less warranty",   
            "Tubular technology Deep cycle design suitable for longer power cuts",
            "Calcium alloy/ultra low maintenance and less topping-up",
            "PE separator - low electrical resistence, minimal self discharging & high porosity",
            "Cell partition welded with short electrical path for low internal resistance",
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
            "DSP based technology design ensures high reliability & rugged performance",
            "T manager (Temperature Manager) a logo inside continuously monitor the temperature of all critical components & protects them from any failure",
            "Inbuilt Solar MPPT based smart charger upto 50Amp",
            "Pure Sine Wave Output (THD<3%)",
            "User friendly interfacing duel display LED & LCD (Both)",
            "Completely Noiseless operation",
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
            "DSP based technology design ensures high reliability & rugged performance",
            "T manager (Temperature Manager) a logo inside continuously monitor the temperature of all critical components & protects them from any failure",
            "Inbuilt Solar MPPT based smart charger upto 50Amp",
            "Pure Sine Wave Output (THD<3%)",
            "User friendly interfacing duel display LED & LCD (Both)",
            "Completely Noiseless operation",    
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
            "Next-GEN Solar Hybrid PCU incorporates DSP based technology",
            "40/50 Amp built-in PWM solar charge controller",
            "Increased battery life as solar panel produces pure DC power",
            "Solar panel 100 W to 800 W (12V) & 200 W - 1600 W (24V)",
            "Solar PV reverse connection protection",
            "Multiple, Multi level inbuilt over current & over voltage protections",
            "Multicolor user friendly interactive LCD display system",
            "Advance pure sine wave technology",
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
            "Next-GEN Solar Hybrid PCU incorporates DSP based technology",
            "40/50 Amp built-in PWM solar charge controller",
            "Increased battery life as solar panel produces pure DC power",
            "Solar panel 100 W to 800 W (12V) & 200 W - 1600 W (24V)",
            "Solar PV reverse connection protection",
            "Multiple, Multi level inbuilt over current & over voltage protections",
            "Multicolor user friendly interactive LCD display system",
            "Advance pure sine wave technology",
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
            "Next-GEN Solar Hybrid PCU incorporates DSP based technology",
            "40/50 Amp built-in PWM solar charge controller",
            "Increased battery life as solar panel produces pure DC power",
            "Solar panel 100 W to 800 W (12V) & 200 W - 1600 W (24V)",
            "Solar PV reverse connection protection",
            "Multiple, Multi level inbuilt over current & over voltage protections",
            "Multicolor user friendly interactive LCD display system",
            "Advance pure sine wave technology",
        ]
    },
    "MPPT 125O": {
        "img": [
            "/static/images/gallery/pic36.png",
        ],
        "oldPrice": "7724",
        "newPrice": "7000",
        "details": [
            "99.97% - 99.99",
        ]
    },
    "LFP MPPT 125O": {
        "img": [
            "/static/images/gallery/pic37.png",
        ],
        "oldPrice": "30 000",
        "newPrice": "28000",
        "details": [
            "Micro-controller Based H-Bridge compact design supported by Microchip ensures high reliability & rugged performance.", 
            "MPPT Solar Charge Controller Inside", 
            "PCU Features Enabled ",
            "LiFepo4 Battery bank inside ",
            "USAN BOLT charging with completes charging time of 5-6 hours (Max.) ",
            "Pollution free/ Environment friendly. No issue of acid fumes ( Safe for Kids & older people)",
            "2000 complete charge discharge cycles No need to replace battery for more than 5 years",
            "Ready to fit Portable model with handle",
            "Dynamic controls algorithm based BMS ensure safety of lithium battery from peak current, peak voltage ripple current ripple voltage and safety for temperature rise.",
            "RCB (Resettable ckt. breaker) peace of mind from hassles of finding fuse in case of excess load more than the capacity of the system is plugged to the system.",
            "Complete Noiseless Operation",
            "Exponential time-based overload protection further ensures reliability of the system.",
        ]
    },
    "LFP HUPS 1250": {
        "img": [
            "/static/images/gallery/pic38.png",
        ],
        "oldPrice": "7724",
        "newPrice": "7000",
        "details": [
            "Micro-controller Based H-Bridge compact design supported by Microchip ensures high reliability & rugged performance.",
            "LiFepo4 Battery bank inside",
            "USAIN BOLT charging with completes charging time of 5.15-7.30 hours (Max.)",
            "Power saving charging, charging the battery more efficiently in less time",
            "Pollution free/ Environment friendly",
            "No hassles of additional Lead Acid Battery connection and periodic maintenance",
            "2000 complete charge discharge cycles",
            "Ready to fit Portable model with handle ",
            "Dynamic controls algorithm based BMS ensure safety of lithium battery ",
            "Adaptive to variable input conditions (rural and urban) wide input range 90V-295V",
            "RCB (Resettable ckt. breaker) peace of mind ",
            "Complete Noiseless Operation",
            "Surge Protection-MOV inside ",
            "T manager (Temperature manager) algorithm monitor the temperature of all critical components and protects them from any failure",
       ]
    },
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
        "emailReceiver": EMAIL_RECEIVER,
        "locationAddress": LOCATION_ADDRESS,
        "locationLink": LOCATION_LINK,
        "facebook": FACEBOOK,
    }
    
    return render(request, "product/home.html", context)

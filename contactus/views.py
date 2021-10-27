from django.shortcuts import render, HttpResponse
import requests
import json
import smtplib
from energysolar.settings import EMAIL_ADDRESS, EMAIL_PASSWORD, EMAIL_RECEIVER, LINKEDIN, LOCATION_ADDRESS, LOCATION_EMBED, LOCATION_LINK, FACEBOOK, TWITTER


# Create your views here.


def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # email verification
        response = requests.get(
            "https://isitarealemail.com/api/email/validate", params={'email': email})
        status = response.json()['status']

        if status != "valid":
            return HttpResponse(json.dumps({"error": "Please Check Your Email-Id"}))

        subject = "Query From Website"
        body = "Message From {} ({})\n\n{}".format(name, email, message)
        emailList = [EMAIL_RECEIVER, ]

        ob = smtplib.SMTP("smtp.gmail.com", 587)
        ob.starttls()
        ob.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        message = "Subject:{}\n\n{}".format(subject, body)
        ob.sendmail(EMAIL_ADDRESS, emailList, message)
        ob.quit()

        return HttpResponse(json.dumps({"status": "success"}))
    else:
        context = {
            "title": "9 Energy Solar",
            "emailReceiver": EMAIL_RECEIVER,
            "locationAddress": LOCATION_ADDRESS,
            "locationLink": LOCATION_LINK,
            "locationEmbed": LOCATION_EMBED,
            "facebook": FACEBOOK,
            "linkedin": LINKEDIN,
            "twitter": TWITTER,
        }
        return render(request, "contactus/home.html", context)

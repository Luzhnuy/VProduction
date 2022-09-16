from django.shortcuts import render, redirect
from .models import AdvertisingRequest
from django.core.mail import send_mail


# Create your views here.
def main(request):
    return render(request, "eng.html", {})


def send_adv_mail(request):
    if request.method == "POST":
        adv_request = AdvertisingRequest()
        adv_request.about_project = request.POST.get("about_project")
        adv_request.advertising = request.POST.get("advertising")
        adv_request.email = request.POST.get("email")
        adv_request.auditory = request.POST.get("auditory")
        adv_request.creative = request.POST.get("creative")
        adv_request.site = request.POST.get("site")
        adv_request.social = request.POST.get("social")
        adv_request.save()
        text = "Client Email: " + adv_request.email + "</br> About Client Project: " \
               + adv_request.about_project + "</br>" + "Client Audience: " \
               + adv_request.auditory + "</br>" + "Client Advertising Examples: " \
               + adv_request.advertising + "</br>" + "What the client want: " \
               + adv_request.creative + "</br>" + "Client site and social networks" \
               + adv_request.site + "</br>" + adv_request.social
        send_mail(
            'New Request On VolstinyProduction',
            text,
            'teamserverr@gmail.com',
            ['teamserverr@gmail.com', 'l.luzhnuy@gmail.com'],
            fail_silently=False,
        )

        return redirect("/")

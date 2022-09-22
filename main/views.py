from django.shortcuts import render, redirect
from .models import AdvertisingRequest, ContactRequest
from django.core.mail import send_mail
import random
import os


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
            fail_silently=True,
        )

        return redirect("/")


def contacting_with_as(request):
    if request.method == "POST":
        contact = ContactRequest()
        contact.full_name = request.POST.get('full_name')
        contact.your_email = request.POST.get('your_email')
        contact.how_can_we_help_you = request.POST.get('how_can_we_help_you')
        contact.file_if_needed = request.FILES.get('file_if_needed')
        # for filename, contact.file_if_needed in request.FILES.iteritems():
        #     name = request.FILES[filename].random()
        #     with open(name, 'rb') as file:
        #         file
        contact.save()
        text = "Client Email: " + contact.your_email + "<br> About Client Project: " \
            + contact.full_name + "<br>" + "Full Name Client: " \
            + contact.how_can_we_help_you + "<br>" + "Help Nedded: " \
            + contact.file_if_needed + "<br>" + "Client Files: "
        send_mail(
            'New Client On VolstinyProduction',
            text,
            contact.your_email,
            ['teamserverr@gmail.com', 'l.luzhnuy@gmail.com'],
            fail_silently=True,
        )

        return redirect("/")


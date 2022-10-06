from django.shortcuts import render, redirect
from .models import AdvertisingRequest, ContactRequest
from django.core.mail import send_mail
from django.conf import settings
import random
import telegram
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
        telegram_settings = settings.TELEGRAM

        text = "***Client Email:*** " + adv_request.email + "\n ***About Client Project:*** " \
               + adv_request.about_project + "\n" + "***Client Audience:*** " \
               + adv_request.auditory + "\n" + "***Client Advertising Examples:*** " \
               + adv_request.advertising + "\n" + "***What the client want:*** " \
               + adv_request.creative + "\n" + "***Client site and social networks***" \
               + adv_request.site + "\n" + adv_request.social

        bot = telegram.Bot(token=telegram_settings['bot_token'])
        bot.send_message(chat_id="@%s" % telegram_settings['channel_name'], text=text)
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
        telegram_settings = settings.TELEGRAM

        text = "***Client Email:*** " + contact.your_email + "\n" + "***Full Name Client:*** " \
            + contact.full_name + "\n" + "***Help Needed:*** " \
            + contact.how_can_we_help_you
        bot = telegram.Bot(token=telegram_settings['bot_token'])
        bot.send_message(chat_id="@%s" % telegram_settings['channel_name'], text=text)

        return redirect("/")


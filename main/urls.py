from django.urls import path
from .views import main, send_adv_mail, contacting_with_as, main_ukr

urlpatterns = [
    path('', main, name="main"),
    path('ukr', main_ukr, name="main_ukr"),
    path("send", send_adv_mail, name="send"),
    path("read_as", contacting_with_as, name="read_as"),
]

from django.urls import path
from .views import main, send_adv_mail

urlpatterns = [
    path('', main, name="main"),
    path("send", send_adv_mail, name="send")
]

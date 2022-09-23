from django.urls import path
from .views import main, send_adv_mail, contacting_with_as

urlpatterns = [
    path('', main, name="main"),
    path("send", send_adv_mail, name="send"),
    path("read_as", contacting_with_as, name="read_as"),
]

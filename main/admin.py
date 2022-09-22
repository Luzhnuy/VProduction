from django.contrib import admin
from .models import AdvertisingRequest, ImgAndVideoUploadGallery, ContactRequest

admin.site.register(AdvertisingRequest)
admin.site.register(ContactRequest)
admin.site.register(ImgAndVideoUploadGallery)
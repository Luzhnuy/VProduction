from django.db import models


class AdvertisingRequest(models.Model):
    email = models.EmailField(null=False)
    your_name = models.TextField()
    telephone = models.TextField()
    short_description = models.TextField()
    select = models.TextField()

    def __str__(self):
        return self.your_name


class ContactRequest(models.Model):
    full_name = models.TextField()
    your_email = models.EmailField(null=False)
    how_can_we_help_you = models.TextField()

    def __str__(self):
        return self.full_name


class ImgAndVideoUploadGallery(models.Model):
    image = models.ImageField(upload_to='static/img/photo_gallery/')
    video = models.FileField(upload_to='static/img/video_gallery/')

    def __str__(self):
        return self.image
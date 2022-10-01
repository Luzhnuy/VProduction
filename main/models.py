from django.db import models


class AdvertisingRequest(models.Model):
    email = models.EmailField(null=False)
    about_project = models.TextField()
    auditory = models.TextField()
    creative = models.TextField()
    advertising = models.TextField()
    site = models.TextField()
    social = models.TextField()

    def __str__(self):
        return self.about_project


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
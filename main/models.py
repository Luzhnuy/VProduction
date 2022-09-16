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


from django.db import models

# Create your models here.

class ContactUs(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField(blank=True)
    phone1 = models.CharField(max_length= 15, blank=True)
    whatsapp_link = models.CharField(max_length=400, blank=True)
    email = models.CharField(max_length=300, blank=True)
    email_link = models.CharField(max_length=400, blank=True)


    footer_details = models.TextField(blank=True)
    twitter = models.CharField(max_length=500, blank=True)
    facebook_link = models.CharField(max_length=500, blank=True)
    insta_link = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.name
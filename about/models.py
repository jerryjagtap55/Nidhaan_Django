from django.db import models
from contact_us.models import ContactUs
# Create your models here.
class About(models.Model):
    about_you = models.CharField(max_length=200, blank=True)
    name = models.CharField(max_length=200)
    profile_pic = models.ImageField(upload_to='photos/%Y/%m/%d/')


    def __str__(self):
        return self.name

class Service(models.Model):
    about = models.ForeignKey(About, on_delete = models.DO_NOTHING, default=1)
    service_title = models.CharField(max_length=500)
    service_description = models.TextField(blank=True)
    show = models.BooleanField(default=True)

    def __str__(self):
        return self.service_title

class Detail(models.Model):
    key = models.ForeignKey(About,on_delete=models.DO_NOTHING, default=1)
    num = models.CharField(max_length=200 ,default=1)
    box_name = models.CharField(max_length=500, blank=True)
    box = models.TextField(blank=True)
    design_name = models.CharField(max_length=500, blank=True)
    design = models.TextField(blank=True)
    graphic_name = models.CharField(max_length=500, blank=True)
    graphic = models.TextField(blank=True)
    creative = models.CharField(max_length=500, blank=True)
    creative_detail = models.TextField(blank=True)

    def __str__(self):
        return self.num

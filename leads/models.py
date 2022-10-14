from email.policy import default
from random import choices
from urllib import request
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from .utils import *
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    is_organisor = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=False)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class LeadManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()


class Lead(models.Model):

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    lead_owner = models.ForeignKey("Agent", null=True, blank=True, on_delete=models.SET_NULL)
    category = models.ForeignKey("Category", related_name="leads", null=True, blank=True, on_delete=models.SET_NULL)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(default = "")
    profile_picture = models.ImageField(null=True, blank=True, upload_to="profile_pictures/")
    converted_date = models.DateTimeField(null=True, blank=True)
    lead_status = models.CharField(max_length = 150, choices = LEAD_STATUS, null=True, blank=True)
    appointment_day = models.CharField(max_length=150, choices = APPOINTMENT_DAYS, null=True, blank=True)
    lead_source = models.CharField(max_length=150, choices = LEAD_SOURCE, null=True, blank=True)    
    ad_source = models.CharField(max_length=150, choices = AD_SOURCE, null=True, blank=True)
    job_title = models.CharField(max_length=150, choices = JOB_TITLE, null=True, blank=True)
    priority = models.CharField(max_length=150, choices = PRIORITY, null=True, blank=True)
    industry = models.CharField(max_length=150, choices = INDUSTRY, null=True, blank=True)
    tier = models.CharField(max_length=150, choices = TIER, null=True, blank=True)
    lead_response = models.CharField(max_length=150, choices = LEAD_RESPONSE, null=True, blank=True)
    currency = models.CharField(max_length=150, choices = CURRENCY, null=True, blank=True)
    secondary_phone = models.CharField(max_length=20, null=True, blank=True)
    secondary_email = models.EmailField(null=True, blank=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    fb_page = models.CharField(max_length=255, blank=True, null=True)
    facebook_ad = models.CharField(max_length=255, blank=True, null=True)
    google_campaign = models.CharField(max_length=255, blank=True, null=True)
    fb_ad_campaign = models.CharField(max_length=255, blank=True, null=True)
    fb_ad_set = models.CharField(max_length=255, blank=True, null=True)
    no_of_employees = models.CharField(max_length=255, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add = True ,null=True, blank=True)


    objects = LeadManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

def handle_upload_follow_ups(instance, filename):
    return f"lead_followups/lead_{instance.lead.pk}/{filename}"

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email


class Category(models.Model):
    name = models.CharField(max_length=30)  # New, Contacted, Converted, Unconverted
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


def post_user_created_signal(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(post_user_created_signal, sender=User)

class Address(models.Model):
    username = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, default="")
    country = models.CharField(max_length=3, choices = COUNTRIES, blank=True, default="")
    state = models.CharField(max_length=124, choices = STATES,blank=True, default="")
    district = models.CharField(max_length=124, choices = DISTRICTS,blank=True, default="")
    postcode = models.CharField(
        _("Post/Zip-code"), max_length=64, blank=True, default=""
    )

    def __str__(self):
        return self.username
    

    def get_complete_address(self):
        address = ""
        if self.address:
            address += self.address
        if self.distict:
            if address:
                address += ", " + self.distict
            else:
                address += self.distict
        if self.state:
            if address:
                address += ", " + self.state
            else:
                address += self.state
        if self.postcode:
            if address:
                address += ", " + self.postcode
            else:
                address += self.postcode
        if self.country:
            print('-----------------------', self.country)
            if address:
                address += ", " + self.country
            else:
                address += self.country
        return address

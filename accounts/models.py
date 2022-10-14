from multiprocessing import parent_process
from django.db import models
from .utils import *
from leads.utils import DISTRICTS, STATES, COUNTRIES
from leads.models import Agent

# Create your models here.

class Account(models.Model):

    account_name = models.CharField(max_length=20)
    job_title = models.CharField(max_length=150, choices = JOB_TITLE, null=True, blank=True)
    age = models.IntegerField(default=0)
    account_owner = models.ForeignKey(Agent, null=True, blank=True, on_delete=models.SET_NULL)
    industry = models.CharField(max_length = 150, choices = INDUSTRIES, null=True, blank=True)
    parent_account = models.CharField(max_length=20, null=True, blank=True)
    lead_source = models.CharField(max_length=150, choices = LEAD_SOURCE, null=True, blank=True)
    co_owner = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(default = "")
    rating = models.CharField(max_length = 150, choices = RATINGS, null=True, blank=True)
    annual_revenue = models.IntegerField(default=0)
    currency = models.CharField(max_length = 150, choices = CURRENCIES, null=True, blank=True)
    facebook_page = models.CharField(max_length=150, null=True, blank=True)
    instagram_page = models.CharField(max_length=150, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    look_up = models.CharField(max_length=150, null=True, blank=True)
    mobile = models.CharField(max_length=150, null=True, blank=True)
    secondary_mobile = models.CharField(max_length=150, null=True, blank=True)              
    secondary_email = models.EmailField(default = "")
    member_status = models.CharField(max_length=150, choices = MEMBER_STATUS, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    district = models.CharField(max_length=150, choices = DISTRICTS, null=True, blank=True)
    state = models.CharField(max_length=150, choices = STATES, null=True, blank=True)
    country = models.CharField(max_length=150, choices = COUNTRIES, null=True, blank=True)
    account_tier = models.CharField(max_length = 150, choices = ACCOUNT_TIER, null=True, blank=True)
    priority = models.CharField(max_length = 150, choices = PRIORITY, null=True, blank=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    employees = models.CharField(max_length=255, blank=True, null=True)
    account_number = models.IntegerField(default=0)
    details_of_competitor_associated = models.CharField(max_length=255, blank=True, null=True)
    exchange_rate = models.CharField(max_length=255, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add = True ,null=True, blank=True)


    def __str__(self):
        return f"{self.account_name}"

def handle_upload_follow_ups(instance, filename):
    return f"lead_followups/account_{instance.account.pk}/{filename}"

class FollowUp(models.Model):
    account = models.ForeignKey(Account, related_name="followups", on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    last_call_date = models.DateTimeField(null = True, blank=True)
    last_connected_call_date = models.DateField(null = True, blank=True)
    last_chat_date = models.DateField(null = True, blank=True)
    last_meeting_date = models.DateField(null = True, blank=True)
    cf_account_status = models.CharField(max_length = 150, choices = CF_ACCOUNT_STATUS, null=True, blank=True)
    follow_up_status = models.CharField(max_length = 150, choices = FOLLOW_UP_STATUS, null=True, blank=True)
    last_project_ref = models.DateField(null = True, blank=True)
    notes = models.TextField(blank=True, null=True)
    file = models.FileField(null=True, blank=True, upload_to='follow_up_files/')

    def __str__(self):
        return f"{self.account.account_name}"
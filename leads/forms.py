from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import Address, Lead, Agent, Category
from accounts.models import FollowUp

User = get_user_model()


class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            'profile_picture',
            'first_name',
            'last_name',
            'age',
            'organisation',
            'lead_owner',
            'lead_status',
            'lead_source',
            'appointment_day',
            'ad_source',
            'job_title',
            'priority',
            'industry',
            'tier',
            'lead_response',
            'currency',
            'description',
            'phone_number',
            'secondary_phone',
            'email',
            'secondary_email',
            'website',
            'fb_page',
            'facebook_ad',
            'google_campaign',
            'fb_ad_campaign',
            'fb_ad_set',
            'no_of_employees'
        )

    def clean_first_name(self):
        data = self.cleaned_data["first_name"]
        # if data != "Joe":
        #     raise ValidationError("Your name is not Joe")
        return data

    def clean(self):
        pass
        # first_name = self.cleaned_data["first_name"]
        # last_name = self.cleaned_data["last_name"]
        # if first_name + last_name != "Joe Soap":
        #     raise ValidationError("Your name is not Joe Soap")

        
class AddressModelForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = (
            'address',
            'country',
            'state',
            'district',
            'postcode',
        )


class LeadForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField(min_value=0)


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}


class AssignAgentForm(forms.Form):
    agent = forms.ModelChoiceField(queryset=Agent.objects.none())

    def __init__(self, *args, **kwargs):
        request = kwargs.pop("request")
        agents = Agent.objects.filter(organisation=request.user.userprofile)
        super(AssignAgentForm, self).__init__(*args, **kwargs)
        self.fields["agent"].queryset = agents


class LeadCategoryUpdateForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            'category',
        )


class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = (
            'name',
        )


class FollowUpModelForm(forms.ModelForm):
    class Meta:
        model = FollowUp
        fields = (
            'notes',
            'file'
        )
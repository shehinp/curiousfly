from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import Account, FollowUp

class DateInput(forms.DateInput):
    input_type = 'date'

class AccountModelForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = (
            'account_name',
            'job_title',
            'age',
            'account_owner',
            'industry',
            'parent_account',
            'lead_source',
            'co_owner',
            'email',
            'rating',
            'annual_revenue',
            'currency',
            'facebook_page',
            'instagram_page',
            'look_up',
            'mobile',
            'secondary_mobile',
            'secondary_email',
            'birthday',
            'member_status',
            'phone',
            'district',
            'state',
            'country',
            'account_tier',
            'priority',
            'website',
            'employees',
            'account_number',
            'details_of_competitor_associated',
            'exchange_rate'
        )
        widgets = {
            'birthday': DateInput(),
        }

class FollowupModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['notes'].required = True

    class Meta:
        model = FollowUp
        fields = (
            'last_call_date',
            'last_connected_call_date',
            'last_chat_date',
            'last_meeting_date',
            'cf_account_status',
            'follow_up_status',
            'last_project_ref',
            'notes',
            'file',
        )
        widgets = {
            'last_call_date': DateInput(),
            'last_connected_call_date': DateInput(),
            'last_chat_date': DateInput(),
            'last_project_ref': DateInput(),
            'last_meeting_date': DateInput(),
        }
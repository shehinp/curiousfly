from django.shortcuts import render, redirect
from .forms import AccountModelForm, FollowupModelForm
from .models import Account, FollowUp
from leads.models import User, Address
from leads.forms import AddressModelForm

# Create your views here.

def account_list(request):
    accounts = Account.objects.all()
    followups = FollowUp.objects.all()
    addresses = Address.objects.all()
    context = {
        "accounts": accounts,
        "followups": followups,
        "addresses": addresses,
    }
    return render(request, "accounts/account_list.html", context)

def account_create(request):
    account = AccountModelForm()
    followup = FollowupModelForm()
    address = AddressModelForm()
    if request.method == "POST":
        account = AccountModelForm(request.POST)
        followup = FollowupModelForm(request.POST)
        address = AddressModelForm(request.POST)
        if account.is_valid() and followup.is_valid() and address.is_valid():
            # print(form.cleaned_data.get('first_name'))
            user_obj = User()
            address_obj = Address()
            followup_obj = FollowUp()

            account_obj = account.save()


            user_obj.first_name = account.cleaned_data.get('account_name')
            user_obj.email = account.cleaned_data.get('email')
            user_obj.username = account.cleaned_data.get('email')
            user_obj.save()

            address_obj.username = account.cleaned_data.get('email')
            address_obj.save()
            address_data = Address.objects.get(username = address_obj.username)
            address_data.address = address.cleaned_data.get('address')
            address_data.country = address.cleaned_data.get('country')
            address_data.state = address.cleaned_data.get('state')
            address_data.district = address.cleaned_data.get('district')
            address_data.postcode = address.cleaned_data.get('postcode')
            address_data.save()

            followup_obj.account = account_obj
            followup_obj.last_call_date = followup.cleaned_data.get('last_call_date')
            followup_obj.last_connected_call_date = followup.cleaned_data.get('last_connected_call_date')
            followup_obj.last_chat_date = followup.cleaned_data.get('last_chat_date')
            followup_obj.last_meeting_date = followup.cleaned_data.get('last_meeting_date')
            followup_obj.last_project_ref = followup.cleaned_data.get('last_project_ref')
            followup_obj.cf_account_status = followup.cleaned_data.get('cf_account_status')
            followup_obj.follow_up_status = followup.cleaned_data.get('follow_up_status')
            followup_obj.file = followup.cleaned_data.get('file')
            followup_obj.notes = followup.cleaned_data.get('notes')
            followup_obj.save()

            return redirect("/accounts")
    context = {
        "account": account,
        "address": address,
        "followup": followup,
    }
    return render(request, "accounts/account_create.html", context)

def account_update(request, pk):
    obj = Account.objects.get(id=pk)
    account = AccountModelForm(instance=obj)
    followup = FollowupModelForm(instance=obj)
    if request.method == "POST":
        account = AccountModelForm(request.POST, instance=obj)
        followup = FollowupModelForm(request.POST, instance=obj)
        if account.is_valid() and followup.is_valid():
            account_obj = account.save()
            followup_obj = FollowUp.objects.get(account = obj)

            followup_obj.account = account_obj
            followup_obj.last_call_date = followup.cleaned_data.get('last_call_date')
            followup_obj.last_connected_call_date = followup.cleaned_data.get('last_connected_call_date')
            followup_obj.last_chat_date = followup.cleaned_data.get('last_chat_date')
            followup_obj.last_meeting_date = followup.cleaned_data.get('last_meeting_date')
            followup_obj.last_project_ref = followup.cleaned_data.get('last_project_ref')
            followup_obj.cf_account_status = followup.cleaned_data.get('cf_account_status')
            followup_obj.follow_up_status = followup.cleaned_data.get('follow_up_status')
            followup_obj.file = followup.cleaned_data.get('file')
            followup_obj.notes = followup.cleaned_data.get('notes')
            followup_obj.save()
            return redirect("/accounts")
    context = {
        "account": account,
        "obj": obj,
        "followup": followup,
    }
    return render(request, "accounts/account_update.html", context)

def account_delete(request, pk):
    account = Account.objects.get(id=pk)
    try:
        user = User.objects.filter(username = account.email)
        address = Address.objects.filter(username = account.email)
        user.delete()
        address.delete()
    except:
        pass
    account.delete()
    return redirect("/accounts")

def account_detail(request, pk):
    account = Account.objects.get(id=pk)
    address = Address.objects.get(username = account.email)
    followup = FollowUp.objects.get(account = account)
    context = {
        "account": account,
        "address": address,
        "followup": followup,
    }
    return render(request, "accounts/account_detail.html", context)

def followup_create(request, pk):
    account = Account.objects.get(id=pk)
    followup = FollowupModelForm()
    if request.method == "POST":
        followup = FollowupModelForm(request.POST)
        if followup.is_valid():
            # print(form.cleaned_data.get('first_name'))
            followup_obj = FollowUp.objects.get(account = account)
            followup_obj.last_call_date = followup.cleaned_data.get('last_call_date')
            followup_obj.last_connected_call_date = followup.cleaned_data.get('last_connected_call_date')
            followup_obj.last_chat_date = followup.cleaned_data.get('last_chat_date')
            followup_obj.last_meeting_date = followup.cleaned_data.get('last_meeting_date')
            followup_obj.last_project_ref = followup.cleaned_data.get('last_project_ref')
            followup_obj.cf_account_status = followup.cleaned_data.get('cf_account_status')
            followup_obj.follow_up_status = followup.cleaned_data.get('follow_up_status')
            followup_obj.file = followup.cleaned_data.get('file')
            followup_obj.notes = followup.cleaned_data.get('notes')
            followup_obj.save()

            return redirect("/accounts")
    context = {
        "account": account,
        "followup": followup,
    }
    return render(request, "accounts/followup_create.html", context)
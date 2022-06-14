from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import *

# Create your views here.

def dashboard(request):
    return render(request, "dashboard.html", {})

def my_ads(request):
    return render(request, "dashboard-myads.html", {})

def my_favorites(request):
    return render(request, "dashboard-myfavorites.html", {})

def offer_messages(request):
    return render(request, "dashboard-offermessages.html", {})

def payments(request):
    return render(request, "dashboard-payments.html", {})

def post_ad(request):
    return render(request, "dashboard-postanad.html", {})

def privacy_settings(request):
    return render(request, "dashboard-privacy-setting.html", {})

def profile_settings(request):
    return render(request, "dashboard-profile-setting.html", {})

def update_user(request):
    if request.method == "POST":
        form = UpdateUserForm(request.POST)

        if form.is_valid():
            return HttpResponseRedirect('/dashboard/profile-settings')

    else:
        form = NameForm()

    return render(request, 'dashboard-profile-setting.html', {'form': form})

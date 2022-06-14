from django.urls import path, include

from .views import *

urlpatterns = [
    path('', dashboard, name="dashboard"),
    path('my-ads/', my_ads, name="my_ads"),
    path('my-favorites/', my_favorites, name="my_favorites"),
    path('offer-messages/', offer_messages, name="offer_messages"),
    path('payments/', payments, name="payments"),
    path('post-ad/', post_ad, name="post_ad"),
    path('privacy-settings', privacy_settings, name="privacy_settings"),
    path('profile-settings', profile_settings, name="profile_settings"),
]

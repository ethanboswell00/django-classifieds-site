# listings/urls.py

from django.urls import path, include
# from rest_framework import routers
from .views import *

# router = routers.DefaultRouter()
# router.register(r'items', views.ItemViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('ad-grid-list/', ad_grid_list, name="ad_grid_list"),
    path('ad-list/', ad_list, name="ad_list"),
    path('ad-details/', ad_details, name="ad_details"),
]

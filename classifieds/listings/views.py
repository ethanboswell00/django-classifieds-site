# views.py

from django.shortcuts import get_object_or_404, render, HttpResponseRedirect

from rest_framework import viewsets

from .serializers import ItemSerializer
from .models import Item

# Create your views here.

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all().order_by('title')
    serializer_class = ItemSerializer

def ad_grid_list(request):
    return render(request, "adlistinggrid.html", {})

def ad_list(request):
    return render(request, "adlistinglist.html", {})

def ad_details(request):
    return render(request, "addetails.html", {})

def create_view(request):
    context = {}

    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "create_view.html", context)

def list_view(request):
    all_listings = Item.objects.all()
    total_listings = all_listings.count()

    context = {'count': total_listings, 'listings': all_listings}

    return render(request, "list_view.html", context)

def update_view(request, id):
    context = {}

    obj = get_object_or_404(Item, id=id)

    form = ItemForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/" + id)

    context["form"] = form

    return render(request, "update_view.html", context)

def delete_view(request, id):
    context = {}

    object = get_object_or_404(Item, id=id)

    if request.method == "POST":
        obj.delete()

        return HttpResponseRedirect("/")

    return render(request, "delete_view.html", context)

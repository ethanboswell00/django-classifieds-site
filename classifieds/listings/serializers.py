# serializers.py

from rest_framework import serializers

from .models import Item

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'title', 'price', 'photo', 'description', 'cell', 'address', 'category', 'available', 'featured', 'liked', 'only_available_on_call', 'created_time', 'last_updated', 'uploaded_by')

from rest_framework import serializers
from .models import Country

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = [
            'id', 'name', 'cca2', 'capital', 'population', 
            'region', 'subregion', 'timezones', 'languages', 
            'flag_png', 'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']

class CountryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name', 'cca2', 'capital', 'population', 'flag_png']
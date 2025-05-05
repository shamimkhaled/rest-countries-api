from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from .models import Country
from .serializers import CountrySerializer, CountryListSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Create your views here.

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({"message": "Country updated successfully.", "data": serializer.data}, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Country deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
    
    
    
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'region', openapi.IN_QUERY,
                description="Region name (e.g. Asia, Europe)",
                type=openapi.TYPE_STRING,
                required=True
            )
        ]
    )
    @action(detail=False, methods=['get'])
    def regional_countries(self, request):
        region = request.query_params.get('region')
        if not region:
            return Response({'error': 'Region parameter is required.'}, status=400)

        regional_countries = Country.objects.filter(region__iexact=region)
        serializer = CountryListSerializer(regional_countries, many=True)
        return Response(serializer.data)
    
    
    
    
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'language', openapi.IN_QUERY,
                description="Language name (e.g. eng, ben, deu)",
                type=openapi.TYPE_STRING,
                required=True
            )
        ]
    )
     
    @action(detail=False, methods=['get'])
    def by_language(self, request):
        language = request.query_params.get('language', '')
        if not language:
            return Response({"error": "Language parameter is required"}, status=400)
        
        countries = Country.objects.filter(languages__has_key=language)
        serializer = CountryListSerializer(countries, many=True)
        return Response(serializer.data)
    



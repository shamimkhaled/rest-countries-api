from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'countries', views.CountryViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.country_list_view, name='country_list'),
    
]
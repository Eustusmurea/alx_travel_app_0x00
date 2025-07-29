from django.urls import path, include
from rest_framework import Router
from .views import ListingViewSet, BookingViewSet

router = Router()
router.register(r'listings', ListingViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

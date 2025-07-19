from rest_framework import serializers
from .models import Listing, Review, Booking, User
from django.utils import timezone

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ['id', 'title', 'description', 'price', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'listing', 'user', 'start_date', 'end_date', 'created_at']
        read_only_fields = ['user', 'created_at']

    def validate(self, data):
        request = self.context.get('request')
        if data.get('user') != request.user:
            raise serializers.ValidationError("You can only create bookings for yourself.")
        
        listing = data.get('listing')
        start_date = data.get('start_date')
        end_date = data.get('end_date')
        overlapping_bookings = Booking.objects.filter(
            listing=listing,
            start_date__lt=end_date,
            end_date__gt=start_date
        ).exclude(id=self.instance.id if self.instance else None)
        if overlapping_bookings.exists():
            raise serializers.ValidationError("This booking overlaps with an existing booking for this listing.")
        return data
    
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'listing', 'user', 'rating', 'comment', 'created_at']
        read_only_fields = ['user', 'created_at']

    def validate(self, data):
        request = self.context.get['request']
        if data.get('user') != request.user:
            raise serializers.ValidationError("You can only create reviews for yourself.")
        

        listing = data.get('listing')
        if not Booking.objects.filter(user=request.user, listing=listing).exists():
            raise serializers.ValidationError("You can only review listings you've booked.")
        return data
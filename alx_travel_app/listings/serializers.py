from rest_framework import serializers
from .models import Listing, Review, Booking
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()


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
        start_date = data.get('start_date')
        end_date = data.get('end_date')
        listing = data.get('listing')

        if end_date <= start_date:
            raise serializers.ValidationError("End date must be after start date.")

        if start_date < timezone.now().date():
            raise serializers.ValidationError("Start date cannot be in the past.")

        overlapping_bookings = Booking.objects.filter(
            listing=listing,
            start_date__lt=end_date,
            end_date__gt=start_date
        ).exclude(id=self.instance.id if self.instance else None)

        if overlapping_bookings.exists():
            raise serializers.ValidationError("This booking overlaps with an existing booking.")
        return data

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'listing', 'user', 'rating', 'comment', 'created_at']
        read_only_fields = ['user', 'created_at']

    def validate(self, data):
        request = self.context.get('request')
        listing = data.get('listing')

        # Check user has booking
        if not Booking.objects.filter(user=request.user, listing=listing).exists():
            raise serializers.ValidationError("You can only review listings you've booked.")
        return data

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

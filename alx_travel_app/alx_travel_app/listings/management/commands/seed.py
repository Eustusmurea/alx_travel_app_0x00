from django.core.management.base import BaseCommand
from listings.models import Listing
from decimal import Decimal
import random

class Command(BaseCommand):
    help = 'Seed the database with sample listings'

    def handle(self, *args, **kwargs):
        titles = [
            "Cozy Apartment", "Beachside Villa", "Mountain Cabin", "Urban Loft",
            "Suburban Home", "Downtown Studio", "Luxury Condo", "Country House",
            "Eco Lodge", "City BnB"
        ]
        descriptions = [
            "A beautiful place to stay.",
            "Close to public transport and restaurants.",
            "Perfect for a weekend getaway.",
            "Enjoy the sunrise with a cup of coffee.",
            "A peaceful place in the heart of the city."
        ]
        prices = [Decimal('50.00'), Decimal('75.00'), Decimal('100.00'), Decimal('120.00'), Decimal('150.00'), Decimal('200.00')]

        for i in range(10):
            listing = Listing.objects.create(
                title=random.choice(titles),
                description=random.choice(descriptions),
                price=random.choice(prices),
            )
            self.stdout.write(self.style.SUCCESS(f"Created listing: {listing.title}"))
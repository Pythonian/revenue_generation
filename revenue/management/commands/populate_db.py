from django.core.management.base import BaseCommand
from random import choice, randint
from faker import Faker
from revenue.models import RevenueCategory, RevenueSource, TaxPayer, RevenueTransaction

fake = Faker()


class Command(BaseCommand):
    help = "Populates the database with revenue categories and sources"

    def handle(self, *args, **kwargs):
        categories = [
            (
                "Tax Types",
                [
                    "Property Tax",
                    "Income Tax",
                    "Sales Tax",
                    "Value Added Tax (VAT)",
                    "Corporate Tax",
                    "Capital Gains Tax",
                ],
            ),
            (
                "Fees and Licenses",
                [
                    "Business License Fee",
                    "Building Permit Fee",
                    "Vehicle Registration Fee",
                    "Marriage License Fee",
                    "Dog License Fee",
                ],
            ),
            (
                "Fines and Penalties",
                [
                    "Parking Fine",
                    "Traffic Violation Fine",
                    "Late Payment Penalty",
                    "Environmental Violation Fine",
                    "Building Code Violation Fine",
                ],
            ),
            (
                "Government Services",
                [
                    "Public Transport Revenue",
                    "Public Utility Revenue",
                    "Library Fees",
                    "Recreational Facility Fees",
                ],
            ),
            (
                "Miscellaneous",
                [
                    "Donations",
                    "Grants",
                    "Fundraising Income",
                    "Rental Income",
                ],
            ),
            (
                "Borrowing",
                [
                    "Loans",
                    "Bond Issuance",
                ],
            ),
            (
                "Other Sources",
                [
                    "Interest Income",
                    "Dividend Income",
                    "Royalty Income",
                ],
            ),
        ]

        for category_name, source_names in categories:
            category, created = RevenueCategory.objects.get_or_create(
                name=category_name
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Successfully populated category: {category_name}"
                    )
                )
            for source_name in source_names:
                source, created = RevenueSource.objects.get_or_create(
                    name=source_name,
                    description="Sample description",
                    category=category,
                )
                if created:
                    self.stdout.write(
                        self.style.SUCCESS(
                            f"Successfully populated source: {source_name}"
                        )
                    )

        tax_payers = []
        for _ in range(50):
            tax_payer_data = {
                "name": fake.name(),
                "address": fake.address(),
                "tin": fake.random_int(min=100000000, max=999999999),
                "phone": fake.phone_number(),
                "email": fake.email(),
                "created": fake.date_between(start_date='-1y', end_date='today')
            }
            tax_payers.append(tax_payer_data)

        for payer_data in tax_payers:
            payer, created = TaxPayer.objects.get_or_create(**payer_data)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Successfully populated: {payer_data['name']}")
                )
            # Create RevenueTransaction for each payer
            for _ in range(randint(1, 50)):
                source = choice(RevenueSource.objects.all())
                # Random amount between 100 and 1000
                amount = randint(100, 1000)
                note = f"Transaction for {source.name}"
                RevenueTransaction.objects.create(
                    tax_payer=payer,
                    revenue_source=source,
                    amount=amount,
                    note=note,
                    created=fake.date_between(
                        start_date='-2y', end_date='today')
                )
                self.stdout.write(
                    self.style.SUCCESS(f"Transaction created: {note}"))

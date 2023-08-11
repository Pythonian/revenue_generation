from django.db import models


class TaxPayer(models.Model):
    name = models.CharField(
        max_length=200,
        unique=True,
        help_text="Business name or Personal name")
    address = models.CharField(max_length=255)
    tin = models.CharField(
        max_length=20, unique=True, help_text="Tax Identification Number"
    )
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    created = models.DateTimeField()
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created"]
        verbose_name_plural = "Tax Payers"

    def __str__(self):
        return self.name

    def get_initials(self):
        words = self.name.split()
        initials = [word[0] for word in words]
        return ''.join(initials)


class RevenueCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created"]
        verbose_name_plural = "Revenue Categories"

    def __str__(self):
        return self.name


class RevenueSource(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    category = models.ForeignKey(RevenueCategory, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created"]
        verbose_name_plural = "Revenue Sources"

    def __str__(self):
        return self.name


class RevenueTransaction(models.Model):
    tax_payer = models.ForeignKey(TaxPayer, on_delete=models.CASCADE)
    revenue_source = models.ForeignKey(RevenueSource, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    note = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created"]
        verbose_name_plural = "Revenue Transactions"

    def __str__(self):
        return f"Transaction {self.id}"

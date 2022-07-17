from django.db import models
from django.core.validators import MinValueValidator

class Size(models.Model):
    size = models.DecimalField(validators=[MinValueValidator(1)], max_digits=2, decimal_places=1)

    def __str__(self) -> str:
        return str(self.size)

class StoreType(models.Model):
    web_type = models.CharField(max_length=10, null=False)

    def __str__(self):
        return self.web_type

class Website(models.Model):
    name = models.CharField(max_length=30, null=False)
    web_type = models.ForeignKey(StoreType, on_delete=models.CASCADE, null=False, related_name="store_type")
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Url(models.Model):
    url = models.CharField(max_length=100, null=False)
    website = models.ForeignKey(Website, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.url

class Data(models.Model):
    website = models.ForeignKey(Website, on_delete=models.CASCADE)
    price = models.IntegerField(validators=[MinValueValidator(1)])
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    retailer = models.CharField(max_length=30, null=False)
    product_type = models.CharField(max_length=20, null=True)
    direct_link = models.CharField(max_length=150)
    stock_code = models.CharField(max_length=10, null=True)









from django.db import models
from django.core.validators import MinValueValidator

class Website(models.Model):
    name = models.CharField(max_length=30, null=False)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Url(models.Model):
    url = models.CharField(max_length=100, null=False)
    website = models.ForeignKey(Website, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.website)

class Image(models.Model):
    image_url = models.CharField(max_length=150)

class Data(models.Model):
    website = models.ForeignKey(Website, on_delete=models.CASCADE)
    price = models.IntegerField(validators=[MinValueValidator(1)])
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    retailer = models.CharField(max_length=30, null=False)
    product_type = models.CharField(max_length=20, null=True)
    direct_link = models.CharField(max_length=150)
    stock_code = models.CharField(max_length=10, null=True)









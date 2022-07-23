from django.db import models
from django.core.validators import MinValueValidator

class Website(models.Model):
    name = models.CharField(max_length=30, null=False)
    status = models.BooleanField(default=False)
    store_url = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Url(models.Model):
    url = models.CharField(max_length=100, null=False)
    website = models.ForeignKey(Website, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.website)

class Data(models.Model):
    product_id = models.CharField(max_length=20)
    title = models.CharField(max_length=150)
    website = models.ForeignKey(Website, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    retailer = models.CharField(max_length=30, null=False)
    product_type = models.CharField(max_length=20, null=True)
    url = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.title

class Variant(models.Model):
    variant_id = models.CharField(max_length=20)
    product = models.ForeignKey(Data, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    sku = models.CharField(max_length=30, null=True)
    featured_image = models.CharField(max_length=150, null=True)
    price = models.IntegerField(validators=[MinValueValidator(1)])
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self) -> str:
        return self.title

class Image(models.Model):
    image_url = models.CharField(max_length=150)
    product = models.ForeignKey(Data, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.product.title










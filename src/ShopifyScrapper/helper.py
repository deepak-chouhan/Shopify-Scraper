from .models import *

# Helper Class for Saving Product
class Product:
    def __init__(self, product, website):
        self.product = product
        self.website = website
        # Database objects
        self.Data_obj = None
    
    def GetLink(self):
        """
        Return Link for Product
        """
        if self.website.store_url[-1] != "/":
            return self.website.store_url + "/products/" + self.product["handle"]
        return self.website.store_url + "products/" + self.product["handle"]
    
    def Data(self):
        """
        Save Product
        """
        # Access attributes using self.product["<attribut>"])
        self.Data_obj = Data(
            product_id = self.product["id"],
            title = self.product["title"],
            website = self.website,
            created_at = self.product["created_at"],
            updated_at = self.product["updated_at"],
            retailer = self.product["vendor"],
            product_type = self.product["product_type"],
            url = self.GetLink(),
        )
        self.Data_obj.save()
    
    def Variants(self):
        """
        Save Products Variants
        """
        if self.product["variants"] and len(self.product["variants"]) > 0:
            for variant in self.product["variants"]:
                variant_obj = Variant(
                    variant_id = variant["id"],
                    product = self.Data_obj,
                    title = variant["title"],
                    sku = variant["sku"] or None,
                    featured_image = variant["featured_image"]["src"] or None,
                    price = float(variant["price"]),
                    created_at = variant["created_at"],
                    updated_at = variant["updated_at"]
                )
                variant_obj.save()

    def ProductImages(self):
        """
        Save Product Images
        """
        if self.product["images"] and len(self.product["images"]) > 0:
            for image in self.product["images"]:
                image_obj = Image(
                    image_url = image["src"],
                    product = self.Data_obj
                )
                image_obj.save()
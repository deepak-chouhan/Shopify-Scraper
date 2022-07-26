import requests
from .models import *
from django.http import HttpResponse

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
                    sku = variant["sku"] or "null",
                    featured_image = variant["featured_image"]["src"] if variant["featured_image"] != None else "null",
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

def Scrape(urls):
    """
    Scrape Data for given URL

    Args:
        urls (list): List of Shopify Store URLS
    """
    for url in urls:
        # TODO: Logic to restart scrapping every 5 min
        
        store_url = url.url + "/products.json?limit=250&page="
        page_no = 1
        has_data = True
        while(has_data):
            page_url = store_url + str(page_no)
            req = requests.get(page_url)
            data = req.json()

            if(len(data["products"]) > 0):
                for product in data["products"]:
                    do_exist = Data.objects.filter(product_id=product["id"]).exists()
                    if do_exist == False:
                        product_obj = Product(product, url.website)
                        product_obj.Data()
                        product_obj.Variants()
                        product_obj.ProductImages()
            else:
                has_data = False
            page_no += 1


def runScrape():
    print("Started")
    urls = Url.objects.filter(website__status=True)
    Scrape(urls)
    print("Finished")

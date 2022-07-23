from .models import *

# TODO: Write Logic to Save the Products in Database
class Product:
    def __init__(self, product):
        self.product = product

        # Database objects
        self.Data_obj = None
        self.Variant_obj = []
        self.Image_obj = []
    
    def Data(self):
        # TODO: Logic to Create Product Data Object
        # Access attributes using self.product["<attribut>"])
        print(self.product["id"])
        print(self.product["title"])
        print(self.product["handle"])
    
    def Variants(self):
        
        # TODO: Logic to Create Variant Data Object and Save them in List
        if self.product["variants"] and len(self.product["variants"]) > 0:
            for i, variant in enumerate(self.product["variants"]):
                print("Variant", i)
                print(variant["id"])
                print(variant["title"])
                print(variant["sku"])
                if variant["featured_image"] != "null":
                    print(variant["featured_image"]["src"])

    def ProductImages(self):

        # TODO: Logic to Create Image Data Object and Save them in List
        if self.product["images"] and len(self.product["images"]) > 0:
            for i, image in enumerate(self.product["images"]):
                print(i, image["src"], len(image["src"]))
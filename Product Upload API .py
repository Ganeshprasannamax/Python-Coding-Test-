# Product Upload Api 
import csv

class Product:
    def __init__(self, name, barcode, brand, description, price, available):
        self.name = name
        self.barcode = barcode
        self.brand = brand
        self.description = description
        self.price = price
        self.available = available
        # If you have Additional Products in Class Add Self.name of the product = product
        # Ex: self.deliverytime = deliverytime 

class ProductInventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_products(self):
        return self.products

class AdminSession:
    def __init__(self):
        self.username = None
        self.logged_in = False

    def upload_products(self, filename):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader) 
            for row in reader:
                name = row[0]
                barcode = row[1]
                brand = row[2]
                description = row[3]
                price = float(row[4])
                available = bool(row[5])
                product = Product(name, barcode, brand, description, price, available)
                product_inventory.add_product(product)

product_inventory = ProductInventory()

admin_session = AdminSession()
admin_session.logged_in = True # Assume admin is already logged in
admin_session.upload_products('products.csv') # Upload products from CSV file

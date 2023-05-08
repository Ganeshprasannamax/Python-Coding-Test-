# Creating New Review Based on Product Purchased.

class Product:
    def __init__(self, name, barcode, brand, description, price, available):
        self.name = name
        self.barcode = barcode
        self.brand = brand
        self.description = description
        self.price = price
        self.available = available
        self.reviews = []
    def add_review(self, user, rating, comment):
        if user.purchased_products.get(self.barcode):
            review = Review(user, rating, comment)
            self.reviews.append(review)
            return "Review added successfully."
        else:
            return "You must purchase this product before leaving a review."
class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        self.purchased_products = {}

    def purchase_product(self, product):
        self.purchased_products[product.barcode] = product
class Review:
    def __init__(self, user, rating, comment):
        self.user = user
        self.rating = rating
        self.comment = comment
# Example usage:

# Selecting Random products
p1 = Product("Product 1", "34567890", "Brand 1", "This is sample description", 200, True)
p2 = Product("Product 2", "4567890", "Brand 2", "This is sample description", 100, False)

# Purchased users 
u1 = User("Ganesh", "Ganeshprasanna@example.com", "password@123")
u2 = User("Steve", "stevewaugh@example.com", "passwOrd123")

# Ganesh purchases Product 1
u1.purchase_product(p1)
# steve  tries to leave a review for Product 1 (but hasn't purchased it)
p1.add_review(u2, 4, "Great product!")  
#Returns "You must purchase this product before leaving a review."

# Ganesh leaves a review for Product 1
p1.add_review(u1, 5, "Awesome product!")  # Returns "Review added successfully."
class Product:
    def __init__(self, name, barcode, brand, description, price, available):
        self.name = name
        self.barcode = barcode
        self.brand = brand
        self.description = description
        self.price = price
        self.available = available
        self.reviews = []

    def add_review(self, user, rating, comment):
        if user.purchased_products.get(self.barcode):
            review = Review(user, rating, comment)
            self.reviews.append(review)
            return "Thanks For Your Reviews & Review added successfully."
        else:
            return "You must purchase this product before leaving a review."


class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        self.purchased_products = {}

    def purchase_product(self, product):
        self.purchased_products[product.barcode] = product

class Review:
    def __init__(self, user, rating, comment):
        self.user = user
        self.rating = rating
        self.comment = comment

# Example usage:
# Create some products
p1 = Product("Product 1", "34567890", "Brand 1", "This is sample description", 200, True)
p2 = Product("Product 2", "4567890", "Brand 2", "This is sample description", 100, False)

# Create some users
u1 = User("Steve", "Steve@example.com", "password")
u2 = User("Bob", "bob@example.com", "password")

# Alice purchases Product 1
u1.purchase_product(p1)

# Bob tries to leave a review for Product 1 (but hasn't purchased it)
p1.add_review(u2, 4, "Great product!")  # Returns "You must purchase this product before leaving a review."

# Alice leaves a review for Product 1
p1.add_review(u1, 5, "Awesome product!")  # Returns "Review added successfully."

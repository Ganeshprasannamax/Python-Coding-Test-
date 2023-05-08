# Creating a Class Product to View a Pagination of the Products 
# In this Api Im using Reviews based Product Pagination , Top Reviews will shows-up
class Product:
    def __init__(self, name, price, barcode, brand, available, description):
        self.name = name
        self.price = price
        self.barcode = barcode
        self.brand = brand
        self.available = available
        self.description = description
        self.reviews = []
# Details from Previous Reviews Results.
    def add_review(self, review):
        self.reviews.append(review)
# Get a Previews review report and Showing most Reviews items in Top to user.
    def get_reviews(self):
        return self.reviews

    def get_average_rating(self):
        if len(self.reviews) == 0:
            return 0
        else:
            total_rating = 0
            for review in self.reviews:
                total_rating += review.rating
            return total_rating / len(self.reviews)

class ProductInventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_products(self, page_size=10, page_number=1, sort_by='average_rating', ascending=False):
        if sort_by == 'average_rating':
            self.products.sort(key=lambda p: p.get_average_rating(), reverse=not ascending)
        elif sort_by == 'price':
            self.products.sort(key=lambda p: p.price, reverse=not ascending)
        else:
            raise Exception('Invalid sort_by parameter')

        start_index = (page_number - 1) * page_size
        end_index = start_index + page_size

        return self.products[start_index:end_index]

class Review:
    def __init__(self, user, product, rating, comment):
        self.user = user
        self.product = product
        self.rating = rating
        self.comment = comment

class ProductViewPaginationAPI:
    def __init__(self):
        self.product_inventory = ProductInventory()

    def add_product(self, product):
        self.product_inventory.add_product(product)

    def get_products(self, page_size=10, page_number=1, sort_by='average_rating', ascending=False):
        return self.product_inventory.get_products(page_size, page_number, sort_by, ascending)

    def review_product(self, user, product, rating, comment):
        review = Review(user, product, rating, comment)
        product.add_review(review)

product_view_api = ProductViewPaginationAPI()

product1 = Product('Product 1', 10.0, '123456789', 'Brand 1', True, 'This is product 1')
product2 = Product('Product 2', 20.0, '234567890', 'Brand 2', True, 'This is product 2')
product3 = Product('Product 3', 15.0, '345678901', 'Brand 3', False, 'This is product 3')


# Adding New Product Reviews 
product_view_api.add_product(product1)
product_view_api.add_product(product2)
product_view_api.add_product(product3)


# User Reviews 
product_view_api.review_product(user1) (product1, 4, 'Great product!')
product_view_api.review_product(user2) (product1, 5, 'Awesome product!')
product_view_api.review_product(user1) (product2, 3, 'Decent product')
product_view_api.review_product(user2) (product2, 2, 'Not good')
product_view_api.review_product(user1) (product3, 1, 'Bad product')
product_view_api.review_product(user2) (product3, 3, 'Average product')

prodcts = product_view_api.get_products(page_size=2, page_number=1, sort_by='average_rating',)
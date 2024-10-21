from astro_shop.models import Product


# sessions
class Cart(object):
    def __init__(self, request):
        self.session = request.session

        # get current session data by session key
        session_data = self.session.get('session_key')

        # if user is new create session key
        if 'session_key' not in request.session:
            session_data = self.session['session_key'] = {}

        # make cart available on each page of site
        self.cart = session_data

    def add(self, product, quantity=1):
        product_id = str(product.id)

        if product_id in self.cart:
            self.cart[product_id] += quantity
        else:
            self.cart[product_id] = quantity  # adding product id with desired quantity

        self.session.modified = True

    def __len__(self):
        return len(self.cart)

    def get_products_with_quantities(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        # Add quantities to the products
        for product in products:
            product.cart_quantity = self.cart[str(product.id)]

        return products

    def update(self, product, quantity):
        product_id = str(product.id)

        if product_id in self.cart:
            self.cart[product_id] = quantity

        self.session.modified = True

    def delete(self, product):
        product_id = str(product.id)

        if product_id in self.cart:
            del self.cart[product_id]
            self.session.modified = True

    def get_total(self):
        products = self.get_products_with_quantities()
        return sum([product.price * int(self.cart[str(product.id)]) for product in products])

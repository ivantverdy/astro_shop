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

    def add(self, product):
        product_id = str(product.id)

        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {'price': str(product.price)}

        self.session.modified = True

    def __len__(self):
        return len(self.cart)
class Cart:
    '''
    Cart class can be used for inherit and overide behaviour
    '''
    def __init__(self,request):
        self.session = request.session
        cart = self.session.get('session_key')
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}
        self.cart = cart

    def add(self,product,qty):
        '''
        updating users' cart session data
        '''
        product_id = product.id
        if product_id not in self.cart:
            self.cart[product_id] = {'price': str(product.price), 'qty':int(qty)}
        self.session.modified = True

    def __len__(self):
        '''
        this function get cart items and count the total items quantity
        '''
        return sum(item['qty'] for item in self.cart.values())

from e_comapp.models import Product

class Cart():
    def __init__(self, request):
        self.session=request.session

        #get the current session key if it exists
        cart=self.session.get('session_key')


        #if the user is new no session key! create one!

        if 'session_key' not in request.session:
            cart=self.session['session_key']={}


        #make sure cart is available on all pages of site
        self.cart=cart



    def add(self, product,quantity):
        product_id = str(product.id)
        product_qty=str(quantity)

        #logic

        if product_id in self.cart:
            pass
        else:
            #self.cart[product_id]={'price': str(product.price)}
            self.cart[product_id]=int(product_qty)



        self.session.modified = True

    def cart_total(self):
        product_ids=self.cart.keys()
        #lookup those keys in our pdt databse model
        products=Product.objects.filter(id__in=product_ids)
        quantities=self.cart
        total=0

        for key, value in quantities.items():
            key=int(key)
            for product in products:
                if product.id==key:
                    total=total+(product.price*value)
        return total          


        



    def __len__(self):
        return len(self.cart)
    
    #tosee the stuff in cart
    def get_prods(self):
        #get ids from cart
        product_ids=self.cart.keys() #fgetting all the ids in add to cart
        #use id to lookup pdts in db model
        products= Product.objects.filter(id__in=product_ids)
        #return those looked up pdts
        return products
    
    def get_quants(self):
        quantities=self.cart
        return quantities
    
    def update(self,product,quantity):
        product_id=str(product)
        product_qty=int(quantity)
        ourcart=self.cart
        ourcart[product_id]=product_qty   
        self.session.modified=True
        thing=self.cart
        return thing
    
    def delete(self,product):
        product_id=str(product)
        #delete from cart
        if product_id in self.cart:
            del self.cart[product_id]

        self.session.modified=True


    
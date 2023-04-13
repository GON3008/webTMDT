from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.SET_NULL,null=True,blank=False)
    name = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    customer_img = models.ImageField(upload_to='customer_img/')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.name
    # @property
    # def ImageURL(self):
    #     try:
    #         url = self.image.url
    #     except:
    #         url = ''
    #     return url


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=200,null=True)
    descriptions = models.TextField()
    image1 = models.ImageField(null=True)
    image2 = models.ImageField(null=True)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null= True,blank=False)

    def __str__(self):
        return self.name
    @property
    # def ImageURL(self):
    #     try:
    #         url = self.image.url
    #     except:
    #         url = ''
    #     return url  
    def ImageURL(self):
       urls = {}
       try:
          urls['image1'] = self.image1.url
       except:
          urls['image1'] = ''
       try:
          urls['image2'] = self.image2.url
       except:
        urls['image2'] = ''
       return urls
 

class ProductSale(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=200,null=True)
    sale = models.CharField(max_length=2)
    descriptions = models.TextField()
    image1 = models.ImageField(null=True)
    image2 = models.ImageField(null=True)
    price = models.FloatField()
    priceDiscount = models.FloatField()
    digital = models.BooleanField(default=False, null= True,blank=False)
    def __str__(self):
        return self.name 
    @property
    # def ImageURL(self):
    #     try:
    #         url = self.image.url
    #     except:
    #         url = ''
    #     return url        

    def ImageURL(self):
       urls = {}
       try:
          urls['image1'] = self.image1.url
       except:
          urls['image1'] = ''
       try:
          urls['image2'] = self.image2.url
       except:
        urls['image2'] = ''
       return urls


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL,blank=True,null=True)
    date_order = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False,null=True,blank=False)
    transaction_id = models.CharField(max_length=200,null=True)

    def __str__(self):
        return str(self.id)
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total 

class OrderItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,blank=True,null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    quantity = models.IntegerField(default=0,null=True,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class ShippingAddress(models.Model):
     customer = models.ForeignKey(Customer, on_delete=models.SET_NULL,blank=True,null=True)
     order = models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
     address = models.CharField(max_length=200,null=True)
     city = models.CharField(max_length=200,null=True)
     state = models.CharField(max_length=200,null=True)
     mobile = models.CharField(max_length=10,null=True)
     date_added = models.DateTimeField(auto_now_add=True)

     def __str__(self):
        return self.address

class Feedback(models.Model):
    name = models.CharField(max_length=200,blank=True,null=True)
    image = models.ImageField(null=True)
    description = models.TextField()
    def __str__(self):
        return self.name 
    @property
    def ImageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url 


class New(models.Model):
    image = models.ImageField(null=True)
    title = models.CharField(max_length=200, blank=True,null=True)
    name = models.CharField(max_length=200,null=True,blank=True)
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    descriptions_title = models.TextField()
    descriptions = models.TextField()
    def __str__(self):
        return self.name 
    @property
    def ImageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url 


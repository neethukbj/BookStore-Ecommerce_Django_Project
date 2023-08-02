from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Collections(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name



class Filter_Price(models.Model):
    FILTER_PRICE = (
        ('0 TO 200','0 TO 200'),
        ('0 TO 400','0 TO 400'),
        ('0 TO 600','0 TO 600'),
        ('0 TO 800','0 TO 800'),
        ('0 TO 1000','0 TO 1000'),
        ('0 TO 2000','0 TO 2000'),
        

    )
    price = models.CharField(choices=FILTER_PRICE,max_length=60)

    def __str__(self):
        return self.price

class Product(models.Model):
    CONDITION =('New','New'),('Old','Old')
    STOCK = ('IN STOCK' ,'IN STOCK'),('OUT OF STOCK','OUT OF STOCK')
    STATUS =('Publish','Publish'),('Draft','Draft')

    unique_id = models.CharField(unique=True,max_length=200,null=True,blank=True)
    image = models.ImageField(upload_to='Product_images/img')
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    condition = models.CharField(choices=CONDITION,max_length=100)
    information = RichTextField(null=True)
    description = RichTextField(null=True)
    stock = models.CharField(choices=STOCK,max_length=200)
    status = models.CharField(choices=STATUS,max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    categories = models.ForeignKey(Categories,on_delete=models.CASCADE)
    collections = models.ForeignKey(Collections,on_delete=models.CASCADE)

    filter_price = models.ForeignKey(Filter_Price,on_delete=models.CASCADE)

    def save(self,*args,**kwargs):
        if self.unique_id is None and self.created_date and self.id:
            self.unique_id = self.created_date.strftime('75%Y%m%d23')+str(self.id)
        return super().save(*args,**kwargs)

    def __str__(self):
        return self.name


class Images(models.Model):
    image = models.ImageField(upload_to='Product_images/img')
    product = models.ForeignKey(Product,on_delete=models.CASCADE)



class Tag(models.Model):
    name = models.CharField(max_length=200)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)

class Contact_us(models.Model):
    email = models.EmailField(max_length=200)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=500)
    lastname = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postcode = models.IntegerField()
    phone = models.IntegerField()
    email = models.EmailField(max_length=100)
    total_amount = models.CharField(max_length=100)
    payment_id = models.CharField(max_length=100,null=True,blank=True)
    paid = models.BooleanField(default=False,null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class OrderItem(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    product = models.CharField(max_length=200)
    image = models.ImageField(upload_to='Product_images/Order_img')
    quantity = models.CharField(max_length=20)
    price = models.CharField(max_length=50)
    total = models.CharField(max_length=100)

    def __str__(self):
        return self.order.user.username

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    product_qty = models.IntegerField(null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)


from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User



# Create your models here.
CATEGORY = (
    ('k' ,'kids'),
    ('w' , 'women'),
    ('m' , 'men')
)

SIZE = (
    ('m' , 'm'),
    ('l','l'),
    ('xl' , 'xl')
)
class Item(models.Model):
    title  = models.CharField(max_length=30)
    category = models.CharField(max_length=30 , choices=CATEGORY)
    image = models.ImageField(upload_to="products" , blank=True , null=True)
    descrption = models.TextField(max_length=400)
    price = models.FloatField()
    size = models.CharField(max_length=20 , choices=SIZE , null=True , blank=True)
    discount_price = models.FloatField(blank=True , null=True)
    slug = models.SlugField(max_length=20)


    def __str__(self):
        return self.title



def save(self, *args, **kwargs):
    self.slug = slugify(self.title)
    super(Item, self).save(*args, **kwargs)



class OrderItem(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordard = models.BooleanField(default=False)
    item = models.ForeignKey(Item , on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"


class Order(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    
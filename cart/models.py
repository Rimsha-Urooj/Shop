from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    quantity = models.IntegerField()
    status = models.BooleanField()

    productImg = models.ImageField(null= True, blank=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    PENDING = 'PENDING'
    COMPLETE = 'COMPLETE'
    DELIVERED = 'DELIVERED'
    ORDER_STATUS = (
        (PENDING, 'Pending'),
        (COMPLETE, 'Complete'),
        (DELIVERED, 'Delivered'),
    )
    total_quantity = models.IntegerField()
    grand_total = models.IntegerField()
    total_discount = models.IntegerField()
    status = models.CharField(max_length=100, choices=ORDER_STATUS)
    product = models.ForeignKey(Product, on_delete=models.PROTECT,default=1)

    def __str__(self):
        return str(self.total_quantity)


class OrderItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    subtotal = models.IntegerField()
    quantity = models.IntegerField()

    def __str__(self):
        return str(self.product)

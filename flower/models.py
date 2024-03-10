from django.db import models

# Create your models here.

class Items(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name
    

class ItemDetails(models.Model):
    name=models.CharField(max_length=50)
    color=models.CharField(max_length=50)
    price=models.FloatField()
    qty=models.IntegerField()
    tax=models.FloatField()
    image=models.CharField(max_length=150)
    total=models.FloatField()
    date=models.DateTimeField(auto_now_add=True)
    itemsid=models.ForeignKey(Items, on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.price
    

class Cart(models.Model):
    id_product=models.IntegerField()
    id_user=models.IntegerField()
    price=models.FloatField()
    qty=models.IntegerField()
    tax=models.FloatField()
    image=models.CharField(max_length=150,null=True)
    total=models.FloatField()
    discount=models.FloatField()
    net=models.FloatField()
    status=models.BooleanField()
    created_at=models.DateTimeField(auto_now_add=True)


class ShippingAddress(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Payment(models.Model):
    name_on_card = models.CharField(max_length=255)
    card_number = models.CharField(max_length=19)  # Including spaces for card readability
    expiry_date = models.CharField(max_length=7)   # MM / YY
    security_code = models.CharField(max_length=4) # CVV
    zip_code = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.name_on_card} {self.card_number}'

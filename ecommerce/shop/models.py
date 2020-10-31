from django.db import models

# Create your models here.
class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=100)
    category=models.CharField(max_length=60,default="")
    subcategory=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=10)
    desc=models.CharField(max_length=400,default="")
    pub_date=models.DateField()
    image=models.ImageField(upload_to="shop/images",default="")

    def __str__(self):
        return self.product_name

class Contact(models.Model):
    msg_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=70)
    email=models.CharField(max_length=40,default="")
    phone=models.CharField(max_length=50,default="")
    message=models.CharField(max_length=500,default="")

    def __str__(self):
        return self.name

class Orders(models.Model):
    order_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=70)
    address=models.CharField(max_length=200)
    state=models.CharField(max_length=40)
    city=models.CharField(max_length=40)
    pincode=models.CharField(max_length=30)
    phone=models.CharField(max_length=15,default='')

    def __str__(self):
        return str(self.order_id)

class orderupdate(models.Model):
    updateid=models.AutoField(primary_key=True)
    orderid=models.IntegerField(default="")
    status=models.CharField(max_length=200)
    timestamp=models.DateField(auto_now_add=True)
    # orderdate=models.DateField(auto_now_add=)

    # def __str__(self):
    #     return self.status[0:12]+ "..."
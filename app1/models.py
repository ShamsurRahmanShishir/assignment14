from django.db import models

# Create your models here.
class microbotics(models.Model):
    customer_id = models.IntegerField()
    customer_name = models.CharField(max_length=50)
    customer_email= models.EmailField(max_length=35)
    batch = models.IntegerField()
    product= models.CharField(max_length=25)



class Info(models.Model):
    First_name = models.CharField(max_length=50)
    Middle_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    
    email = models.EmailField(max_length=20)
    serial = models.IntegerField(max_length=40)
    password = models.CharField(max_length=40)
    re_password = models.CharField(max_length=40)
    textarea = models.CharField(max_length=50)
    Checkbox = models.CharField(max_length=50)
    payments = models.DecimalField(max_digits=6,decimal_places=2)
    django = models.BooleanField()

    





    



    
    

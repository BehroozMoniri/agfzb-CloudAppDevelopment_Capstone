from django.db import models
from django.utils.timezone import now
from django.conf import settings
# Create your models here.
import uuid


# <HINT> Create a Car Make model `class CarMake(models.Model)`:
class CarMake(models.Model):
    # carmake_id = models.AutoField(primary_key=True)
    id = models.AutoField(primary_key=True, editable=False, null=False)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    #  carmodel_id = models.ForeignKey(CarModel , on_delete=models.CASCADE)
    def __str__(self):
        return self.name 

# <HINT> Create a plain Python class `CarDealer` to hold dealer data
class CarDealer(models.Model):
    # cardealer_id = models.AutoField(primary_key=True)
    id = models.AutoField(primary_key=True, editable=False, null=False)
    full_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    zip = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    # review = models.ManyToManyField(DealerReview)
    def __str__(self):
        return self.full_name 
# <HINT> Create a Car Model model `class CarModel(models.Model):`:
class CarModel(models.Model):
    # carmodel_id = models.AutoField(primary_key=True)
    # car_make = models.ManyToOneField(CarMake )
    id = models.AutoField(primary_key=True, editable=False, null=False)
    name = models.CharField(max_length=100)
#  Make model (One Car Make has many Car Models, using ForeignKey field)
    car_make = models.ForeignKey( CarMake , on_delete=models.CASCADE) 
# - Dealer id, used to refer a dealer created in cloudant database
    car_dealer  = models.ForeignKey(CarDealer , on_delete=models.CASCADE)
    
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
    year = models.DateField()
    def __str__(self):
        return self.name
# <HINT> Create a plain Python class `DealerReview` to hold review data
class DealerReview(models.Model):
    id = models.AutoField(primary_key=True, editable=False, null=False)
    car_dealer  = models.ForeignKey(CarDealer , on_delete=models.CASCADE)
    car = models.ForeignKey(CarModel  , on_delete=models.CASCADE)
    purchasecheck = models.BooleanField(default=False)
    purchasedate = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE ) #, through='Users' 
    content = models.TextField(max_length=1000)
    def __str__(self):
        return self.content
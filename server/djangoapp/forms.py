from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CarMake, CarDealer, CarModel


class CarForm(ModelForm):
    class Meta:
        model = CarMake

class CarDealerForm(ModelForm):
    class Meta:
        model = CarDealer

class CarModelForm(ModelForm):
    class Meta:
        model = CarModel
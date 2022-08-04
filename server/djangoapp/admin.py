from django.contrib import admin
from .models import  CarDealer, CarMake, CarModel, DealerReview
# Register your models here.

class CarDealerInline(admin.StackedInline):
    model = CarDealer
    extra = 2
# CarModelInline class
class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 2

# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]

# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]
# Register models here

admin.site.register(CarDealer)
admin.site.register(DealerReview)
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel) #, CarModelAdmin

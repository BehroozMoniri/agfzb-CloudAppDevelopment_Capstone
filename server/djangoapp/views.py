from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from .models import CarDealer , CarModel, CarMake, DealerReview 
# from .restapis import related methods
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json
from django.urls import reverse 

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Create an `about` view to render a static about page
def about(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/about.html', context)
        

# Create a `contact` view to return a static contact page
def contact(request ): # ,dealer_id
    context = {}
    # dealer = get_object_or_404(CarDealer, pk=dealer_id)
    # address = dealer.address
    # context['address'] = address
    if request.method == "GET":
        return render(request, 'djangoapp/contact.html', context)
        #return HttpResponseRedirect(reverse(viewname='djangoapp:contact')) # , args=(dealer.id )
# Create a `login_request` view to handle sign in request
# def login_request(request):
# ...
def registration_request(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'djangoapp/registration.html', context)
    elif request.method == 'POST':
        # Check if user exists
        username = request.POST['username']
        password = request.POST['psw']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        user_exist = False
        try:
            User.objects.get(username=username)
            user_exist = True
        except:
            logger.error("New user")
        if not user_exist:
            user = User.objects.create_user(username=username, 
                                            first_name=first_name, 
                                            last_name=last_name,
                                            password=password)
            login(request, user)
            return redirect("djangoapp:index")
        else:
            context['message'] = "User already exists."
            return render(request, 'djangoapp/registration.html', context)

def login_request(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['psw']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('djangoapp:index')
        else:
            context['message'] = "Invalid username or password."
            return render(request, 'djangoapp/login.html', context)
    else:
        return render(request, 'djangoapp/login.html', context)

def logout_request(request):
    logout(request)
    return redirect('djangoapp:index')



# Update the `get_dealerships` view to render the index page with a list of dealerships
def get_dealerships(request):
    context = {}
    dealer_list = CarDealer.objects.all()
    context["dealership_list"] = dealer_list 

    if request.method == "GET":
        return render(request, 'djangoapp/index.html', context)


# Create a `get_dealer_details` view to render the reviews of a dealer
def get_dealer_details(request, dealer_id):
    dealer = get_object_or_404(CarDealer, pk=dealer_id)
    dealer_list = CarDealer.objects.all()
    #comments = dealer.dealerreview_set.all().get(cardealer_id=dealer_id)
    context = {"dealer" : dealer , "dealer_list" :dealer_list} #, "comments":comments
    if request.method == "GET":
        return render(request, 'djangoapp/dealer_details.html', context)
    

# Create a `add_review` view to submit a review
def add_review(request, dealer_id): #, review_id 
    dealer = get_object_or_404(CarDealer, pk=dealer_id)
    cars =  CarModel.objects.all()
    context = {"dealer" : dealer, "cars": cars}
    if request.method == "GET":
        # print(context)
        # return HttpResponse('<h1>Heloo</h1>')
        return render(request, 'djangoapp/add_review.html', context)

    if request.method== "POST":
        comment = request.POST['content']
        purchasecheck = request.POST['purchasecheck']
        purchasedate = request.POST['purchasedate']
        car_id = request.POST['car']
        car = CarModel.objects.filter(id = car_id) #.values_list('choices',flat = True)
        review = DealerReview.objects.create(car_dealer_id =dealer_id, 
                                    purchasecheck=purchasecheck, 
                                    purchasedate=purchasedate,
                                    car_id = car_id,
                                    user=request.user, 
                                    content=comment )
        review.save()
        return HttpResponseRedirect(reverse('djangoapp:dealer_details', args=(dealer_id,)))
        #return HttpResponseRedirect(reverse(viewname='djangoapp/dealer_details.html', args=(dealer_id,)))
    #return redirect('djangoapp:index')

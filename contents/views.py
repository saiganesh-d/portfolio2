from django.contrib.auth.models import User
from django.http import FileResponse, Http404
from django.shortcuts import render, get_object_or_404
from os.path import splitext
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
import joblib

# Create your views here.
def city(request):

  
    rf=joblib.load('final.sav')
    if request.method == "GET":
        return render(request,"contents/city.html")

    
       
    Year =request.POST['Year']
    Present_Price =request.POST['Present_Price']
    Kms_Driven =request.POST['Kms_Driven']
    Owner =request.POST['Owner']
    Fuel_Type_Petrol =request.POST['Fuel_Type_Petrol']
    Seller_Type_Individual =request.POST['Seller_Type_Individual']
    Transmission_Mannual =request.POST['Transmission_Mannual']
    Year= int(Year)
    Year= 2021-Year
    Present_Price=float(Present_Price)
    
    if(Fuel_Type_Petrol=='Petrol'):
        Fuel_Type_Petrol=1
        Fuel_Type_Diesel=0
    else:
        Fuel_Type_Petrol=0
        Fuel_Type_Diesel=1
    if(Seller_Type_Individual=='Individual'):
        Seller_Type_Individual=1
    else:
        Seller_Type_Individual=0
    if(Transmission_Mannual=='Mannual'):
        Transmission_Mannual=1
    else:
        Transmission_Mannual=0



    prediction=rf.predict([[Year,Present_Price,Kms_Driven,Owner,Fuel_Type_Diesel,Fuel_Type_Petrol,Seller_Type_Individual,Transmission_Mannual]])
    output=round(prediction[0],2)
    if output<0:
        return render(request,"contents/city.html",{"prediction_texts":"Sorry you cannot sell this car"})
    else:
            return render(request,"contents/city.html",{"prediction_text":"You Can Sell The Car at {}".format(output)})




def home(request):
    
    return render(request, 'contents/portfolio.html')




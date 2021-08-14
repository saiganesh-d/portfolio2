from django.contrib.auth.models import User
from django.http import FileResponse, Http404
from django.shortcuts import render, get_object_or_404
from os.path import splitext
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
import joblib
import pandas as pd
from blog import views


# Create your views here.
def sales(request):
    LR=joblib.load('sales.sav')
    rf=joblib.load('sales2.sav')
    if request.method == "GET":
        return render(request,"contents/sales.html")
    Item_Identifier=request.POST['Item_Identifier']
    Item_Weight=request.POST['Item_Weight']
    Item_Fat_Content=request.POST['Item_Fat_Content']
    Item_Visibility=request.POST['Item_Visibility']
    Item_Type=request.POST['Item_Type']
    Item_MRP=request.POST['Item_MRP']
    Outlet_Identifier=request.POST['Outlet_Identifier']
    Outlet_Establishment_Year=request.POST['Outlet_Establishment_Year']
    Outlet_Size=request.POST['Outlet_Size']
    Outlet_Location_Type=request.POST['Outlet_Location_Type']
    Outlet_Type=request.POST['Outlet_Type']
    typereg=request.POST['typereg']
    print(Outlet_Type)
    a,b,c,d,e,f,g,h,i,j=0,0,0,0,0,0,0,0,0,0
    type1, type2, type3,small, medium,large=0,0,0,0,0,0
    p,q,r,x,y,z,z1,reg=0,0,0,0,0,0,0,0
    lo=0

    if(Outlet_Identifier=='a'):
        a=1
    if(Outlet_Identifier=='b'):
        b=1
    if(Outlet_Identifier=='c'):
        c=1
    if(Outlet_Identifier=='d'):
        d=1
    if(Outlet_Identifier=='e'):
        e=1
    if(Outlet_Identifier=='f'):
        f=1
    if(Outlet_Identifier=='g'):
        g=1
    if(Outlet_Identifier=='h'):
        h=1
    if(Outlet_Identifier=='i'):
        i=1
    if(Outlet_Identifier=='j'):
        j=1
    if(Outlet_Location_Type=='type1'):
        type1=1
    if(Outlet_Location_Type=='type2'):
        type2=1
    if(Outlet_Location_Type=='type3'):
        type3=1
    if(Item_Type=='F'):
        q=1
    if(Item_Type=='D'):
        p=1
    if(Item_Type=='NC'):
        r=1
    if(Outlet_Size=='small'):
        small=1
    if(Outlet_Size=='medium'):
        medium=1
    if(Outlet_Size=='large'):
        large=1
    if(Outlet_Type=='g'):
        x=1
    if(Outlet_Type=='h'):
        y=1
    if(Outlet_Type=='i'):
        z=1
    if(Outlet_Type=='j'):
        z1=1
    if(Item_Fat_Content=='LF'):
        lo=1
    else:
        reg=1
    if(typereg=='h'):
        pre=LR.predict([[Item_Weight,Item_Visibility,Item_MRP,lo,reg,type1, type2, type3,small,medium,large,p,q,r,x,y,z,z1, a,b,c,d,e,f,g,h,i,j]])
    else:    
        pre=rf.predict([[Item_Weight,Item_Visibility,Item_MRP,lo,reg,type1, type2, type3,small,medium,large,p,q,r,x,y,z,z1, a,b,c,d,e,f,g,h,i,j]])
    print([Item_Weight,Item_Visibility,Item_MRP,lo,reg,type1, type2, type3,small,medium,large,p,q,r,x,y,z,z1, a,b,c,d,e,f,g,h,i,j])
    print([9.3,
        0.016047301,
        249.8092,
        1,
        0,
        1,
        0,
        0,
        0,
        1,
        0,
        0,
        1,
        0,
        0,
        1,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        1])
    prediction=round(pre[0],2)
    return render(request,"contents/sales.html",{'prediction':prediction})

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

def ipl(request):
    return render(request, "contents/ipl.html")




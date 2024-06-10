from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Farmer_db, Crop_db
from django.contrib.auth.hashers import make_password, check_password

def home(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        # Handle form submission for registration
        username = request.POST['username']
        email = request.POST['email']
        passw = request.POST['password1']
        passv = request.POST['password2']

        if passw != passv:
            return render(request, 'registration.html', {'ok': 'Passwords do not match'})
        
        if Farmer_db.objects.filter(name=username).exists():
            return render(request, 'registration.html', {'ok': 'Username already exists'})

        # Hash the password before saving it
        hashed_password = make_password(passw)
        
        my_user = Farmer_db.objects.create(name=username, email=email, password=hashed_password)
        my_user.save()
        
        return render(request, 'index.html',{'mas':'Registration done successfully!,please login'})
    
    return render(request, 'registration.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password1']
        
        try:
            user = Farmer_db.objects.get(email=email)
            if check_password(password, user.password):
                request.session['user_id'] = user.id
                return render(request, 'welcome.html',{'user':user.name})
            else:
                return render(request, 'login.html', {'error': 'Invalid login credentials'})
        except Farmer_db.DoesNotExist:
            return render(request, 'login.html', {'error': 'Invalid login credentials'})
    
    return render(request, 'login.html')



def add_crop(request):
    user_id = request.session.get('user_id')
    if user_id:
        if request.method == 'POST':
            farmer = Farmer_db.objects.get(id=user_id)
            crop_name = request.POST['crop_name']
            land_siz = request.POST['land_size']
            planting_date = request.POST['planting_date']
            harvest_date = request.POST['harvest_date']
            yield_amount = request.POST['yield_amount']
            
            Crop_db.objects.create(farmer=farmer, crop_name=crop_name, land_size=land_siz, planting_date=planting_date, harvest_date=harvest_date, yield_amount=yield_amount)
            return render(request, 'welcome.html', {'message': 'Crop '+crop_name+' added successfully!', 'user': farmer.name})
        return render(request, 'add_crop.html')
    return render(request,'welcome.html')



def search(request):
    user_id = request.session.get('user_id')
    if user_id:
        farmer = Farmer_db.objects.get(id=user_id)
        crops = Crop_db.objects.filter(farmer=farmer)
        return render(request, 'search_results.html', {'crops': crops})
    return render(request,'welcome.html')
def fertilizer_suggest(request):
    return render(request,'fertilizer_suggest.html')
def logout(request):
    return render(request,'index.html',{'logout_mass':'you have logout successfully!!!'}) 
def welcome(request): 
    user_id = request.session.get('user_id') 
    if user_id:
        farmer = Farmer_db.objects.get(id=user_id)
        return render(request,'welcome.html',{'user':farmer.name})




    
    

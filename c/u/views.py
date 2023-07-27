from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from u.models import candidate,worker,search
from django.contrib import messages
from django.contrib.auth import authenticate,login

import sqlite3 as db
import pandas as pd  
import numpy as np 
from fuzzywuzzy import fuzz


def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['email']
        mobile =request.POST['mobile']
        password=request.POST['password']
        password1=request.POST['password1']

        if password == password1:
            if User.objects.filter(username = username).exists():
                messages.info(request,'username already exist')
                return redirect('register')

            # elif User.objects.filter(email = email).exists():
            #     messages.info(request,'email already exist')
            #     return redirect('register')

            else:
                user = User.objects.create_user(username=username,password=password,email=username,first_name=first_name,last_name=last_name)
                user.save()
                user_details = User.objects.get(username = username) 
                user1 = candidate(email=username,name=first_name,mobile = mobile,user_id = user_details.id)
                user1.save()
                print("user created")
                return redirect('login')
        else:
            return redirect('register')
    else:    
        return render(request,"candidate/can.html")
def log_view(request):
    if request.method == "POST":
        username=request.POST['email']
        print(username)
        password=request.POST['password']
        print(password)
        user=authenticate(request,username=username, password=password )
        print(user)
        if user is not None:
            login(request,user)
            return redirect('index')
        messages.success(request,("please give correct information"))
        return redirect('login')
    return render(request,"candidate/test.html") 
def index_view(request):
        if request.method == "POST":
            searchs=request.POST['message'] 
            current_user = request.user  
            use_id=current_user.id
            print(use_id)
            use = search(message=searchs, userid = use_id)
            use.save()
            d=searchs
            if d=="mobile":
                con = db.connect('db.sqlite3')
                s= pd.read_sql_query("SELECT * FROM mobile;", con)
                print(s)
            else:
                a=fuzz.ratio(d, "mobile")
                print(a)
                if a >= 80:
                    con = db.connect('db.sqlite3') 
                    s= pd.read_sql_query("SELECT * FROM mobile;", con)
                    
                    print (s)
        return render(request,"candidate/test2.html") 	
def wregister(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['email']
        mobile =request.POST['mobile']
        password=request.POST['password']
        password1=request.POST['password1']
        designation=request.POST['designation']

        if password == password1:
            if User.objects.filter(username = username).exists():
                messages.info(request,'username already exist')
                return redirect('wregister')

            # elif User.objects.filter(email = email).exists():
            #     messages.info(request,'email already exist')
            #     return redirect('register')

            else:
                user = User.objects.create_user(username=username,password=password,email=username,first_name=first_name,last_name=last_name)
                user.save()
                user_details = User.objects.get(username = username) 
                user1 = worker(email=username,name=first_name,mobile = mobile,designation=designation,user_id = user_details.id)
                user1.save()
                print("user created")
                return redirect('login')
        else:
            return redirect('register')
    else:    
        return render(request,"candidate/register.html")
# def search(request,pk):
#     if request.method == "GET":
#         searchs=request.GET['message']   
#         use = search(message=searchs,userid = pk)
#         use.save()
#         return redirect('login')
#     return render(request,"candidate/test2.html") 
    
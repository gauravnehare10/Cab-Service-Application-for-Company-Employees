from django.shortcuts import render, redirect
from cabservice.models import *
from cabservice.forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request, 'cabserv/index.html')

def loginview(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        pwd = request.POST.get('password')
        user = authenticate(request, username=uname, password=pwd)
        if user is not None:
            login(request, user)
            msg = 'Logged in successfully'
            return redirect('/')
        else:
            msg = 'Invalid username or password'
            return redirect('/login')
    return render(request, 'cabserv/auth/login.html')

def registerview(request):
    form = CustomUserForm()
    if request.method == "POST":
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            msg = 'Registered Successfully! Login to Continue...'
            return redirect('/login')
    return render(request, 'cabserv/auth/register.html', context={'form': form})

def logoutview(request):
    if request.user.is_authenticated:
        logout(request)
        msg = 'Logged out Successfully'
        return redirect('/')

@login_required
def emp_profile(request):
    current_user = request.user
    user_id = current_user.id
    employee = Employee.objects.filter(user_id=user_id).first()
    return render(request, 'cabserv/profile/emp_prof.html', context={'employee': employee})

@login_required
def update_profile(request):
    employee, created = Employee.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = EmpProfileForm(request.POST, instance=employee)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.user = request.user
            employee.save()
            return redirect('emp_prof')
        else:
            print(form.errors)
    else:
        form = EmpProfileForm(instance=employee)

    return render(request, 'cabserv/profile/edit_prof.html', {'form': form})

@login_required
def booking(request):
    if request.method == "GET":
        form = BookingForm()
        print("hiii")
        return render(request, 'cabserv/booking.html', context={'form': form})
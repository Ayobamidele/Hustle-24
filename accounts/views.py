from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import Group

# Create your views here.
from .models import *
from .forms import *
from .decorators import *

# @allowed_users(allowed_roles=['Customer'])
@unauthenticated_user
def registerPageCustomer(request):
	form = CreateUserForm()
	if request.method == "POST":
		print(request.POST)
		post = request.POST.copy() # to make it mutable
		post.update({'username': str(post['first_name'] + " " + post['last_name'])})
		form = CreateUserForm(post)
		if form.is_valid():
			# or set several values from dict
			print(post)
			print(form)
			username = post['first_name'] + " " + post['last_name']
			new_user = User.objects.create_user(username= username,
												email=post['email'],
												password=post['password1'],
												first_name=post['first_name'],
												last_name = post['last_name']
												)
			new_user.save()
			messages.success(request, 'Account was created for ' + username)
			return redirect('login')
	context = {'form': form}
	return render(request, 'accounts/register_customer.html', context)

@with_usertype(allowed_roles=['Customer'])
def registerPageVendor(request):
	form = CreateUserForm()
	if request.method == "POST":
		print(request.POST)
		post = request.POST.copy() # to make it mutable
		post.update({'username': str(post['first_name'] + " " + post['last_name'])})
		form = CreateUserForm(post)
		if form.is_valid():
			# or set several values from dict
			print(post)
			print(form)
			username = post['first_name'] + " " + post['last_name']
			new_user = User.objects.create_user(username= username,
												email=post['email'],
												password=post['password1'],
												first_name=post['first_name'],
												last_name=post['last_name'],
												is_vendor=True,
												is_customer=False,
												)
			new_user.save()
			messages.success(request, 'Account and Shop was created for ' + username)
			return redirect('login')
	context = {'form': form}
	return render(request, 'accounts/register_vendor.html', context)

@unauthenticated_user
def loginPage(request):
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request,user)
			for group in request.user.groups.all():
				if 'Vendor' == str(group):
					return redirect('home')
					# return redirect('vendor')
				else:
					return redirect('home')
					# return redirect('customer')
		else:
			messages.info(request, 'Username OR password is incorrect')
	return render(request,'accounts/login.html')



def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
@allowed_users(allowed_roles=['Customer'])
def customerPage(request,pk):
	customerId = Customer.objects.filter(id=pk)
	customer = request.user.customer
	print(pk)
	context = {	"customer": customer,
				"id": customerId,}
	return render(request,'accounts/customer.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Vendor'])
def vendorPage(request,pk):
	vendorId = Vendor.objects.get(id=pk)
	vendor = request.user.vendor
	context = {	"customer": vendor,
				"id": vendorId,}
	return render(request,'accounts/account_settings.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Customer'])
def accountSettings(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)
    if request.method == "POST":
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
    context = {"form": form}
    return render(request,'accounts/account_settings.html',context)
from django.test import TestCase
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.contrib import messages
from accounts.forms import CustomerForm

# Create your tests here.

# @login_required(login_url='login')
# @allowed_users(allowed_roles=['Customer'])
# def customerPage(request,customer):
# 	customer = request.user.customer
# 	form = CustomerForm(instance=customer)
# 	if request.method == "POST":
# 		form = CustomerForm(request.POST, request.FILES, instance=customer)
# 		if form.is_valid():
# 			form.save()
# 	context = {	"customer": customer,"form": form,}
# 	return render(request,'accounts/customer.html',context)

# def customerPage(request,customer):
# 	customer = request.user.customer
# 	form = CustomerForm(instance=customer)
# 	if request.method == "POST":
# 		form = CustomerForm(request.POST,request.FILES,instance=customer)
# 		if form.is
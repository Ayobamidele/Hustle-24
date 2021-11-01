from django.test import TestCase
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.contrib import messages

# Create your tests here.

# def loginPage(request):
#     if request.method == "POST":
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request,user)
#             return redirect('home')
#         else:
#             messages.info(request, 'Username OR password is incorrect')
#     context = {}
#     return render(request,'accounts/login.html', context)
def loginPage(request):
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request,user)
			for group in request.user.groups.all():
				if 'Vendor' == str(group):
					return redirect('vendor-page')
				else:
					return redirect('customer-page')
		else:
			messages.info(request, 'Username OR password is incorrect')
	return render(request,'accounts/login.html')
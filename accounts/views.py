from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

# Create your views here.
from .models import *
from .forms import *

def registerPage(request):
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
			return redirect('home')
	context = {'form': form}
	return render(request, 'accounts/register.html', context)
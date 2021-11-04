from django.shortcuts import render
from django.shortcuts import render
from .models import *
from accounts.models import *
from django.shortcuts import get_object_or_404

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required


# Create your views here.
from django.contrib.auth import get_user_model
from .decorators import *

# Create your views here.

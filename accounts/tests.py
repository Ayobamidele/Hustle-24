from django.test import TestCase
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.contrib import messages
from accounts.forms import CustomerForm

# Create your tests here.
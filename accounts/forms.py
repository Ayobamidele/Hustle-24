from django import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import *

GENDER = (
    ('Male', 'male'),
    ('Female', 'female')
)


class AnonymousUserForm(ModelForm):
    class Meta:
        model = AnonymousUsers
        fields = ['email']

    def __init__(self, *args, **kwargs):
        super(AnonymousUserForm, self).__init__(*args, **kwargs)
        for field in self.fields.keys():
            self.fields[field].widget.attrs.update({'class': 'form-control '})


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username' , 'first_name' , 'last_name' , 'email']

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field in self.fields.keys():
            self.fields[field].widget.attrs.update({'class': 'form-control'})
            self.fields[field].required = False


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        for field in self.fields.keys():
            self.fields[field].widget.attrs.update({'class': 'form-control'})
            self.fields[field].required = False


class VendorForm(ModelForm):
    class Meta:
        model = Vendor
        fields = '__all__'
        exclude = ['user', 'orders']

    def __init__(self, *args, **kwargs):
        super(VendorForm, self).__init__(*args, **kwargs)
        for field in self.fields.keys():
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        for field in self.fields.keys():
            self.fields[field].widget.attrs.update(
                {'class': 'input', 'placeholder': f'{field}'.capitalize()})

    # def clean_username(self):
    # 	user_name = self.cleaned_data['username'].lower()
    # 	r = Customer.objects.filter(username=user_name)
    # 	if r.count():
    # 		raise forms.ValidationError("Username already exists")
    # 	return user_name

    # def clean_password2(self):
    # 	cd = self.cleaned_data
    # 	if cd['password'][0] != cd['password2'][1]:
    # 		raise forms.ValidationError('Passwords do not match.')
    # 	return cd['password2']

    # def clean_email(self):
    # 	email = self.cleaned_data['email']
    # 	if Customer.objects.filter(email=email).exists():
    # 		raise forms.ValidationError(
    # 			'Please use another Email, that is already taken')
    # 	return email


class ChangeUserPasswordForm(UserCreationForm):
    class Meta:
        model = User
        # fields = '__all__'
        fields = ['password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(ChangeUserPasswordForm, self).__init__(*args, **kwargs)
        # self.fields['password1'].widget.attrs.update({'placeholder': 'New Password'})
        # self.fields['password2'].widget.attrs.update({'placeholder': 'Re-type New Password'})
        for field in self.fields.keys():
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError(
                "Sorry, that login was invalid. Please try again.")
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user


class AccountAuthenticationForm(forms.ModelForm):
    """
      Form for Logging in  users
    """
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'password')
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        """
          specifying styles to fields 
        """
        super(AccountAuthenticationForm, self).__init__(*args, **kwargs)
        for field in self.fields.keys():
            self.fields[field].widget.attrs.update(
                {'class': 'input', 'placeholder': f'{field}'.capitalize()})

    def clean(self):
        if self.is_valid():

            email = self.cleaned_data.get('email')
            password = self.cleaned_data.get('password')
            if not authenticate(email=email, password=password):
                raise forms.ValidationError('Invalid Login')


class ChangePictureForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['profile_pic']

    def __init__(self, *args, **kwargs):
        super(ChangePictureForm, self).__init__(*args, **kwargs)
        self.fields['profile_pic'].widget.attrs.update(
            {'style': 'display: none;'})
        for field in self.fields.keys():
            self.fields[field].widget.attrs.update({'class': 'autosubmit'})

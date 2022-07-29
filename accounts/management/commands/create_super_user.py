from ...models import *
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
import getpass
import re
# elif re.search('[A-Z]',password) is None:
#     print("Make sure your password has a capital letter in it")

def validate(comfirm=False):
	if comfirm:
		password = getpass.getpass('Password (Recomfirmed):')
	else:
		password = getpass.getpass("Password:")
	while True:
		if len(password) < 8:
			print("Make sure your password is at lest 8 letters")
		elif re.search('[0-9]', password) is None:
			print("Make sure your password has a number in it")
		else:
			print("Your password seems fine")
			return password
			break


class Command(BaseCommand):
	help = 'Create custom super user'

	def handle(self, *args, **kwargs):
		user_name = input("Username:")
		email = input("Email:")
		first_name = input("Firstname:")
		last_name = input("Lastname:")
		password = validate()
		recomfirmed_password = validate(True)
		if password == recomfirmed_password:
			print(user_name, password, recomfirmed_password)
			super_user = User.objects.create_superuser(username= user_name,email=email,password=password,
			first_name=first_name,last_name=last_name)
			super_user.save()
			# Customer.objects.create(user=super_user, username=user_name, email=email,
									# firstname=first_name, lastname=last_name)
			# Customer.save()

## Hustle-24

E-commerce website for Vendors and Customers.



# Getting Started
Here are instructions in getting your code up and running on your own system. 
1. Installation
2. Package dependencies
3. Latest releases

## Installations
After cloning or downloading the repo I highly recommend creating a virtual environment to avoid any errors. Also download from the main branch, other branches under the develop branch may give errors due to some features still under develpment. You will be updated when the branches under develop are finally ready to  be merged to the main branch.

Use this command to clone:
```console
git clone https://github.com/Ayobamidele/hustle_24.git
```
or

Use this link for download:
``` console
https://github.com/Ayobamidele/hustle_24.git
```

You must have installed Python and Django to run the project and most importantly Pip for the next instruction and as said earlier a virtual environment.
 Need help installing the above follow these instructions:

 ## Installing Python
Need help installing Python, follow the instructions found in the link below:
 ```
 https://github.com/PackeTsar/Install-Python
 ```

 ## Instlling Pip
 Follow the instructions found in the link below to install pip:
 ```shell
 https://pip.pypa.io/en/stable/installation/
 ```
## Installing Django
Django 3.2 will be installed in the requirements.txt when the pip command in package dependencies is run. If you want to install the latest version run this command
```shell
python -m pip install Django
```
## Creating a Virtual Environment
Follow the instructions found in the link below to create a virtual environment to run the project and install packages:
```shell
https://gist.github.com/MichaelCurrin/3a4d14ba1763b4d6a1884f56a01412b7
```

After completing this part follow the next instructions.
## Package dependencies
To run the program you'll need to download some packages first. Run this command to install the packages in requirements.txt:
```shell
pip install -r requirements.txt
```
## Run Project

Now run this command to run the project after succesfully installing the package dependencies.
```shell
python manage.py runserver
```


You should then be able to view the project from the browser using the link provided in the terminal
## Latest releases
During the creation of this project python 3.10 was available but python 3.8 was used to avoid any issues with support. All versions 3.+ should work.

# Build and Test
Testing the project is still in development using pytest and coverage package to ensure all functions are up and running to avoid by error and early detection. Testing will be released soon.



# Features
1. Products
2. Payment
3. Admin
4. User
5. Orders

### Products

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The database allows for multiple products to have multiple attributes. Allowing for a product to have different attributes. Products can have categories, picture, quantity, price and discount price by default. Products can also be deactivated or activated to display when needed.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The website loads products from a SQLite database and displays them. Users can select display products in a single category - *which are set active in the database*. Users can click on any product to get more information including pricing and other available details. Users can select items and add them to their shopping cart. There they can checkout having the options to pay with Paypal or email. If you don't want to buy yet, you could save to your wishlist for later

### Payment

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;User payment address and card details is saved on the site for fast checkout. Users have the options to pay with:

- Paypal
- Email

### Admin


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Superusers can access the admin page. The page is enabeled with filtering and ordering, so searching through various data objects is fast and easy.

### User


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Users have easy access to the login and register page and if any issue with their password they have the option to reset it with their email. Some personal details can also be added.

> **Note:** Once users register their account, the email won't be removed from the database if you try to delete the account. 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Also after registering you can't change the email used to register.

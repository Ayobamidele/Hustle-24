## Hustle-24

E-commerce website for Vendors and Customers.



# Getting Started
Here are instructions in getting your code up and running on your own system. 
1. Installation & Downloads
2. Package dependencies
3. Latest releases

## Installations & Downloads
To run this project yolu woud need to Download and install varoius
appications and packages

##  Installing Virtual Studio code
To download the application use the official  Virtual
Studio code website and choose your operating system whether it be
Windows, Mac or Linux. Once downloaded, please install.
The link below:
``` link
https://code.visualstudio.com/download
```
## Downloading the Project
There are two options for downloading this project from Github


1. Download zip (This is way more easier trust me.)
2. Clone


## Download zip
Follow this link for download:
``` console
https://github.com/Ayobamidele/Hustle-24/tree/main
```
Then follow these instructions:
1. Navigate to the “<>Code” tab.

2. Click on the “Code” button on the right. A dropdown should appear.

3. In the “Clone” menu, under the “HTTPS” tab, click on “Download ZIP”

## Clone
To download the package use the official Git website and choose
your operating system whether it be
Windows, Mac or Linux.


Use this link below:
``` link
https://git-scm.com/download/linux
```


## Install Git on Windows

1. Navigate to the latest Git for Windows installer and download the latest version.
2. Once the installer has started, follow the instructions as provided in the Git Setup wizard screen until the installation is complete.
3. Open the windows command prompt (or Git Bash if you selected not to use the standard Git Windows Command Prompt during the Git installation).
4. Type ```git version``` to verify Git was installed.

Note: 
```git-scm``` is a popular and recommended resource for downloading Git for Windows. The advantage of downloading Git from ```git-scm``` is that your download automatically starts with the latest version of Git included with the recommended command prompt, Git Bash . The download source is the same Git for Windows installer as referenced in the steps above.
Install Git on Mac


## Install Git on Mac

Most versions of MacOS will already have Git installed, and you can activate it through the terminal with ```git version```. However, if you don't have Git installed for whatever reason, you can install the latest version of Git using one of several popular methods as listed below:


## Install Git From an Installer
If you get confused in the first instruction skip to Installing Git from Homebrew

1. Navigate to the latest macOS Git Installer and download the 
latest version.

2. Once the installer has started, follow the instructions as 
provided until the installation is complete.

3. Open the command prompt "terminal" and type git version to 
verify Git was installed.

Note: ```git-scm``` is a popular and recommended resource for 
downloading Git on a Mac. The advantage of downloading Git from 
```git-scm``` is that your download automatically starts with the 
latest version of Git. The download source is the same macOS Git Installer as referenced in the steps above.

## Install Git from Homebrew

Homebrew is a popular package manager for macOS. If you already have Homwbrew installed, you can follow the below steps to install Git and if not go to the official Homebrew and copy the command to install Homebrew:

1. Open up a terminal window and install Git using the following 
command: ```brew install git```.
2. Once the command output has completed, you can verify the 
installation by typing: git version.


If not 









Clone from the main branch, other branches under the develop branch may give errors due to some features still under develpment. You will be updated when the branches under develop are finally ready to  be merged to the main branch.

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
After cloning or downloading the repo I highly recommend creating
a virtual environment to avoid any errors.
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

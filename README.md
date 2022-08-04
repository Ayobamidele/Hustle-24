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
To clone the project you would need to have installed Git 
Then follow these instructions to use this command to clone:
1. Follow this link:
https://github.com/Ayobamidele/Hustle-24/tree/main
2. Navigate to the “<>Code” tab.

3. Click on the “Code” button on the right. A dropdown should appear.

4. In the “Clone” menu, under the “HTTPS” tab, click on the copy
clipboard icon

5. Open your terminal and type theis command ```git clone``` 

6. Then paste into the termial and click enter. (It should then look like the command below)

```console
git clone https://github.com/Ayobamidele/Hustle-24.git
```


You must have installed Python and Django to run the project and most importantly Pip for the next instruction and as said earlier a virtual environment.


 Need help with the installtion the follow the instructions below



 ## Installing Python
Need help installing Python, follow the instructions below:
## **Windows**
1. If you have not yet installed Python on your Windows OS, then download and install the latest Python3 installer from [Python Downloads Page](https://www.python.org/downloads/)
   - Make sure to check the box during installation which adds Python to PATH. Labeled something like **Add Python 3.X to PATH**

2. Once Python is installed, you should be able to open a command window, type `python`, hit ENTER, and see a Python prompt opened. Type `quit()` to exit it. You should also be able to run the command `pip` and see its options. If both of these work, then you are ready to go.
  - If you cannot run `python` or `pip` from a command prompt, you may need to add the Python installation directory path to the Windows PATH variable
    - The easiest way to do this is to find the new shortcut for Python in your start menu, right-click on the shortcut, and find the folder path for the `python.exe` file
      - For Python2, this will likely be something like `C:\Python27`
      - For Python3, this will likely be something like `C:\Users\<USERNAME>\AppData\Local\Programs\Python\Python37`
    - Open your Advanced System Settings window, navigate to the "Advanced" tab, and click the "Environment Variables" button
    - Create a new system variable:
      - Variable name: `PYTHON_HOME`
      - Variable value: <your_python_installation_directory>
    - Now modify the PATH system variable by appending the text `;%PYTHON_HOME%\;%PYTHON_HOME%;%PYTHON_HOME%\Scripts\` to the end of it.
    - Close out your windows, open a command window and make sure you can run the commands `python` and `pip`

## **MacOS** 
MacOS comes with a native version of Python. As of this writing, it comes with a version of Python2, which has been deprecated. In order to use most modern Python applications, you need to install Python3. Python2 and Python3 can coexist on the same machine without problems, and for MacOS it is in fact necessary for this to happen, since MacOS continues to rely on Python2 for some functionality.

There are a couple of ways we can install Python3 on your MacOS operating system:

### Option 1: Install the official Python release
1. Browse to the [Python Downloads Page](https://www.python.org/downloads/)
2. Click on the "Download Python 3.x.x" button on the page
3. Walk through the steps of the installer wizard to install Python3
4. Once installed, the wizard will open a Finder window with some `.command` files in it
    - Double-click the `Install Certificates.command` file and the `Update Shell Profile.command` file to run each of them
    - Close the windows once they are finished
6. Open your **Terminal** application and run the command `python3` to enter the Python interactive command line. Issue the command `quit()` to exit. Also make sure PIP (the Python package manager) is installed by issuing the command `pip3 -V`. It should display the current version of PIP as well as Python (which should be some release of Python3).
7. You're all done. Python is installed and ready to use.

### Option 2: Install with Homebrew
[Homebrew](https://brew.sh/) is a MacOS Linux-like package manager. Walk through the below steps to install Homebrew and an updated Python interpreter along with it.

1. Open your **Terminal** application and run: `xcode-select --install`. This will open a window. Click **'Get Xcode'** and install it from the app store.
2. Install Homebrew. Run: `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
   - You can also find this command on the [Homebrew website](https://brew.sh/)
3. Install latest Python3 with `brew install python`
4. Once Python is installed, you should be able to open your **Terminal** application, type `python3`, hit ENTER, and see a Python 3.X.X prompt opened. Type `quit()` to exit it. You should also be able to run the command `pip3` and see its options. If both of these work, then you are ready to go.
  - Here are some additional resources on [Installing Python 3 on Mac OS X](https://docs.python-guide.org/starting/install3/osx/)

## **Linux**
- **Raspberry Pi OS** may need Python and PIP
  - Install them: `sudo apt install -y python3-pip`
- **Debian (Ubuntu)** distributions may need Python and PIP
  - Update the list of available APT repos with `sudo apt update`
  - Install Python and PIP: `sudo apt install -y python3-pip`
- **RHEL (CentOS)** distributions usually need PIP
  - Install the EPEL package: `sudo yum install -y epel-release`
  - Install PIP: `sudo yum install -y python3-pip`


 ## Instlling Pip
 Follow the instructions found below to install pip depending on your operating system:
 ### **Linux/Mac**
```terminal
 $ python -m ensurepip --upgrade
 ```

 ### **Windows**
```terminal
C:> py -m ensurepip --upgrade
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

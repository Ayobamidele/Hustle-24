# Hustle_24

E-commerce website for vendors to sell products to the world.


# Functions
Here are some Function the project would accompish. 
1. Businesses can sell and Track sales of products
2. Customers can buy Products without registeration
3. Moderators can disable Content

## User Types
1. Customers
2. Vendors
3. Moderators(Super users)


# Features For Vendor
1. Create and manage multiple Products
2. Creae Shops that manange orders, payment and Track sales
3. Create one-time shops to sell products as limited offers
4. Disable/Enable multiple Payment methods for recieving payment
3. Create watch list for products so other users can tag on to be notified when offers will be available

# Features For Customer
1. View, Track and Buy Products
2. Revsit Orders made
3. Write Reies for products bought
4. Disable/Enable multiple Payment Cards
5. Tag watchlist



# Technologies
1. HTML & CSS
2. JS
3. Django
4. Python
5. Ajax

# Payment
1. Paypal
2. Stripe
3. Creditcard


# Database
The database for development is **sqlite** but for Production either mongoDB or Postgres

# Data models
1. User
2. Customer
3. Vendor
4. Shop
5. Product
6. Product Category
7. Product Images
8. Reviews
9. Product Specification
10. Cart
11. Cart Item
12. Order
13. Order Item
14. Shipping Address
15. Shipping Payment
16. Watch List
17. Watched Product




## User
This is the base model for a user type. This model allows for one or more user types to be
created for one user but still have that user linked to each one of those types so a user 
can easily have multiple roles in the application without creating a new accounf for each 
user type each time. 

This model controls actions like;
1. Authentication
2. Login
3. Creation of accounts
4. Permisssions
5. Roles

## Customer
This model contains the essential details about a customer like Credit Card and Phone number. 
Customers can perform actions like:
1. Purchasing Products
2. Tagging Products
3. Create watchlists
4. Edit Account
5. Delete Account
6. Customer can view / search products without login .
7. Customer can also add / remove product to cart without login
8. Customer can check their ordered details by clicking on orders button .
9. When customers try to purchase products they can login to purchase or do so anonymously .
10. Customer can see the order status ( Pending , Confirmed , Delivered ) for each order
11. Customer can Download their order invoice for each order
12. Customer can send feedback to admin / vendor.




## Vendor
Vendors model can only be created by a Customer, without it accessing various urls will
be unaccessable. By default a Shop model is assigned and created for a vendor on creation.
vendors can perform actions such as
1. Create/Edit/Disable Products
2. Analyse sales
3. Enable Payment methods
4. Edit Shop Profile
5. Create Watchlists

## Shop
Shop model is what gives permission and allows Vendors to perform any action.
Actions performed in shop range from starting a campaign to creating discount
sales for products. Shop model is where features are released to Vendors. All
actions by the vendor are performed in the shop.


## Product
The model contains details of a product from the vendor. Product does not 
perform any action except performinng simple calculations and taking note of
customers that tag it.



## Product Category
Category models allow sor customers to understand the subject of the Product
being sold also gies the search engine data to go through. Categiory does not
perform any actions except listing products that use the tag.




## Product Images
Product images model stores image for a product with the a key linked to a product
allowing for mulltiple images to linked to a product




## Reviews
Reviews model hold data for the reviews left by Customers who have purchased the product.
A Review can only be created if the Customer has purchased that item previously. Any 
Customer that made a review about a Product can only edit it or delete it. 






## Product Specification
Product Specification  holds details of products. It's done this way so Vendors
have a customizable data entry for their Products since all Products have different
specification that differs from the other.





## Cart
Cart model stores the the items each user add to a cart and tracks the quantity
and price ot each item. It also perform a sorting action by sending orders to 
the items vendors when payment and delivery details are recieved.



## Cart Item
Cart Item model contains detail about the item in the cart acting as a link to
the product added.



## Order
Order model contains data about purchase orders.


## Order Item
Order Item has the data of products in the order.



## Shipping Address
Shipping Address model stores data on addresses for delivery.



## Shipping Payment
Shipping Payment model stores data on card details for making payment.



## Watch List
Watch List model stores data of tracked Products.Users can have multiple watchlists.



## Watched Product
Watched Product model stores the data on the products added to the Watch List.





# Apps

## Accounts
This app controls tasks relating to the user activities and manages funtions such as authentication, login and
registration, the app manages user permissions to view page and User creation.




## Api
Api app handles all requests to the api enpoints.



## Carts
The Carts app handles the actions of the cart and cart item models Carts app also has
the funtionality to sort cart items to send orders to the vendors


# Orders
Orders app manages orders by customer. It also handels payment and address details for an order checking and verifying 
that the data received are in the right format. It also manages the status of the delivery.


# Shop
Shop app manage tools used by vendors to track Product sales, Product details and also manages orders recieved
from Customers. Shop has tools that can tracks sales, views and customer response for one or more products. Shop gives 
vendors the benefit of comparing one or more product sales against other products in your inventory.


# Watched Product
Watched Product app helps with keeping track of intrested product for customers, showing changes in price ,stock or ratings
helping you get an idea of the product you are inntrested in buying. Watched products notifies vendors of customers who tag
their products 


# Diagrams

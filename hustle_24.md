# Hustle_24

E-commerce website for creating communities for vendors to sell products to the world and customers to get Great deals.

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
2. Revisit Orders made
3. Write Reviews for products bought
4. Disable/Enable multiple Payment Cards
5. Tag watchlist

# Plans
1. Be able to sell tickets



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
[User Diagrams](https://viewer.diagrams.net/?tags=%7B%7D&highlight=0000ff&edit=_blank&layers=1&nav=1&title=H24%20-%20User.drawio#R%3Cmxfile%20pages%3D%223%22%3E%3Cdiagram%20id%3D%22WVeWZBNY8nBaMOHt7w_k%22%20name%3D%22Anonymous%20User%22%3E7VpZd%2BI2GP01PGaOVwyPCSGZJXOaJm3aPs1RbGErkS2PLLPk11eyJbxCOYkxDAVygvVpsXS%2Fq6t1YE7C5S0FcfCdeBAPDM1bDszrgWGMDGMg%2FjRvlRss284NPkVebtILwyN6g9KoSWuKPJhUEjJCMENx1eiSKIIuq9gApWRRTTYjuPrWGPiwYXh0AW5a%2F0IeC2SzbK2wf4bID9SbdU3GhEAlloYkAB5ZlEzmdGBOKCEsfwqXE4gFdgqXPN%2FNhth1xSiM2C4ZyAgsXp%2BeYu%2Fuxzf%2FDlp%2FfI1mF9I7c4BT2WBZWbZSCECPAyKDEYn4zxUlaeRBUa7GQ4SygPgkAviOkJgbdW58gYytpDtBygg3BSzEMnZGIiYjdVOGJwQTWryj2TzZ4oSk1JV1%2B2G8PNyuZi%2B%2FTe3Pb2H8sprAbxeKJoD6kG1pu0wn2ld6gQTvFpIQMrriCSjEgKF5lRBA8spfpyug5w8S%2FXZPjEcLYj2jS98Ct8HvX7%2B8vKXPqjY9Am93jXJ7OvuoYO6f3z3BfFxsNnuBmaNJV3%2BL%2FJ%2FGhgr%2Fk4V1Y6wM10v5hjy0KofuIUW8xZBKY%2F%2BOc47Kb9aJdg9zdFQw2ycKc%2BdaL7PeE8SrbGhyVmmoSZacVJqWVi0ir6jMVfPVuhrvd9%2FwIO4rqZ1jVdVu7NjvUbsehiWzH0aYepURxrBfRjgn2qHHRyWbo18T5X2T3zKq5NfNfsmv5p6HXEXatVXkwDBvsk%2FX3aQdAe2o%2BoluHd4hw8M6pPNxZ1eHbKt2xR9DzBtw5aF5xS%2FDn6nYEMqgu0gyLC95At2JlxlwKp4%2F%2BeL3kvtuFZI0UQXy%2BmVl5tFdvebPhE8aZFnP9ENFbapojZ9JAOKMZS4T%2FLlaBIjBxxhk9FhQENeohzAuUW1miy%2B3J4ySV1iKGWYfHuNT4CFYIehz9uVxACM%2F4jaXx4vZUoXZjgrLyrbsxCl%2FQ8rgciv%2FlITXZ7RK0hfFpqOa5Aal%2Fcb6xLczxtoNxj5AHyUCjYaSYIziBP63jxqoRnAxLcnQwCnRpdCngkGCWOv4iCG2esi6L4mmLamNSRFIuGKwS7EfvKG4TALb88LIe2fOBPqh4EQ5oxgqSknclM655FZSDJxr%2FsQohDcEeyjyJX7C8p3MC0MHxDPrvLMbvFtvaZeJ59h7Ip6zUSrjVtnBKIIXqmZCeLRPdrtSep54N4NhIkYQwv%2B5nBRlVWsIVLxRns6k%2F4VJr9cmzLa%2BK%2Bv3JbfjFrkNCZ%2BWGNoXydgZJeGas2c2ng4bnboGa82xv182tizoph4SK86fKcicLkqIzmz8H7DRGh2cjWaDjXfEF%2FQ78%2B50eKfbtU2sXVVwb0sgvbkGmgTQfSUpOyvfCTJwWFuDiyPkAzOwOS18QpCjr91T4qUuG8gLTGcenhAPTafKQ2dHIbTHe6KhOjwv0TBfTItiDW3TSmUBmBtcYJR8QCe7gLN2NGiPWhZ7Rguea5A%2FAui2m2clPB8hoG7AbTeEFt1bgAkiL8N4zjt%2B8n4g227cqU4udvsxeIb4CrivfnYKsOtlvN3dYA%2Brbhi2je9tbqif5HZ3SqI13KC2fgQ6Amh1HVVJgd7cVmoIchKQeOumUl74R%2FeVtu9Id7MUqPUcfdgyIPbrsuZSQOI%2FAQz6hCK4xz7SAaRWFVFjj52AB4vLxflRb3FD25z%2BCw%3D%3D%3C%2Fdiagram%3E%3Cdiagram%20id%3D%22FTO33HKffsncvfsBfMTp%22%20name%3D%22Customer%22%3E7V1bc9o4FP41PKbjO%2FCYAG13Np3NJp1u%2B9RRbAHeGouVRUL661eyJd8kwATfAiEzCTqWLft83zmSjo6cgTlZbT9hsF5%2BQR4MBobmbQfmdGAYumOa9A%2BTvCQSSwgW2Pd4pUzw4P%2BGXKhx6cb3YFSoSBAKiL8uCl0UhtAlBRnAGD0Xq81RUGx1DRZQEjy4IJCl%2F%2FgeWSbSka1l8s%2FQXyxFy7rGj6yAqMwF0RJ46DknMmcDc4IRIsm31XYCA6Y8oZfkvI87jqY3hmFIqpyw2Vw9fr53bg3rD%2Bx8%2FXk7Xl8Nr%2FhVIvIiHhh69Pl5EWGyRAsUgmCWSW8w2oQeZFfVaCmrc4vQmgp1KvwXEvLCwQQbgqhoSVYBP0pvGL985%2BfHhR%2Bs8MEWxek2f3D6wkvyE4vbRxvswj2POebMAXgByT51GElFpoRcC1yhnyBaQXpDtAKGASD%2BU5EkgHNtkdZLT71DPr1nQ%2BN24ZicFNwqbMEacYnkTvlZGajXGIOXXLU1qxDtbse2i%2B1YVokjx9WnX5I7EKWcTjJRzLsjOGh0y8GMdgkLneHoAA%2Fj0h3EPn1yiOsiZ4lzVdjqNEJOSy%2BSwDSqkbMuPpgSH05He%2BsTDrbNiwnYpiHKGdas8JIr1I70YWDtut1QAaNjAbHqB6QFHZq90qHdqZPTe9fRar1Cx3mTDNd7pcNhk27bKrpta3i82871%2BM64aA%2Fj4SGL6E2XbzXS5RujUpfvtNvlj5LWnkCw4Y%2FQhbtswWSHvTJZoeZ9ej9Zq3MUEn6QTq%2BS8gQFCMfXN7X404r2jX45TMM%2BjvUhCmuheR4Qs1tArH4BcqQbagKQsoXwNrKe0Cn1hH2cvxj9cnOm3j2uZUPjbTSPhdmvkbYI%2F14mFrWHF6tigX%2FPhj%2F1v4g7%2FXYLRjN3%2B%2BPPdF5%2F7lAon71f0YGxhMRkExF6cSwhEi3BOtarS5jGbp6XPoEPaxBr5RmDdUnZfhDkOve5zX6oPCIY%2FYK5I078oUcWGHg%2BLAwJHuMfegwE%2FiKkMpceZ%2F1JAcuhKPObVaxQCEcMMYHbvXrnR81xKSAtYpHP2WIMj1Fry9w6jKU1hJQIXOShwhAQSGUPS2oBkgUFgb%2BO4GGkJN2G8Dk3vZkOhtQsnP82bL3oJrPLVDQwr3PHQ%2BKTl%2FuYvCicKWobk6wQUXMh12y1bMflYrNUnwtD75VnRnCxYszIn8jUm6vibvATdTWFGoPhlH4jGMKPKPD8cMH1xyRf0FMmqIN%2Bh9mXLvi1Qz%2FVUMYJmG7WBd4JjQV%2BCK%2FErVFctCT6l4fEWbC%2F157HGidwFTH%2Fiegvl7JCXP0Ri4pCQu9%2FncneWf%2FmWM8WzYMAUJi8KrZgaEVjcKoaw7AxY5DDF%2FdwhZ6YL%2F6DE3mO0Sql8jtJ3xxJd9LRGb7SN9t2U3SUpzYzz2dR1v82IAadXSF8Z%2BM5srGUOJEmUuTZaCjYWA6018dGeXZ3ixYx%2FdiFDY2W0OadhmdFQ71EQ0Mfdz1glYPckyV0f8XUe3eEZ8dA2%2BodAx2Jgd98SLWv3WHkbVwy4Fmg7zw8Ix6mK9iCh1rV4eG4KR4OJR4mc%2B6kO941c%2FkHEHd5FfjRCY6yDn3aFWZ%2FqgGOXk5trW%2B5bncsxPOflNEQFp68iuJ4JYuF6OZ6O1AFQ9KQXoJNMoxPwx7x1YvBkFMbzKOsbue12Kui7cIx7V0NPMLnlyMDVteDX0O1tJHolT1%2FJaiMXdxgwxda4S%2FssfC89pmChtg9p7glTdQOXDGS%2FzH%2BDI6J5PPFlTIDRLWpj6HLOp24KmbINRBDtZ3OySE74oIZc4vEfuwB7uETHS1EFcw%2FEc0RzoYW6WnK8Gkz9p2jiQfnYBOQOkhSAxHKc2Rj3DUTBDVVizl5z69NYeDTB423XngehlH0Buy6Aciczo1XLKHnIHuAALvLgtFdAjZm2ZoUE62moNm3pC6HPykuVJEnTLDeMCytWsz67quu%2Ff45vZ%2B5Lvzz083j97tRH7I8xqlqpYznAzkeyidSJEsr65lqoGpP6dh3k2eZ0qFYSpRw3GMgRQsZDWULaSqlYzdNVIHyEkxHOKlh7TAVURDmdBIQRilEMh517ar6kBF9nK866IOMZjZslKfcul5eZU%2B8aB07NtRGI2%2BZagKZ1%2B5gyyOq1dv72BWRH3bZ%2B8iGlA7C1MHuc3NullU2EFUAuFXvpsgP6Ll3O2gLw4q2kGTqdGUMcrxnolp3PDcTKO3p0402cxLUNNj%2FupHaO43yux2O6DRqNhRFWnr%2FOg1T3sLbCDx8L5P4nuvRd%2B9jeuUrYxocB1SF1G4J0r9N5%2FvN7fVHGGm%2F4JfZRvc%2B2Yq5Tetdjt242pVP3laPo2xc3s9xKWofdenAZLV%2Fple%2BlCFvub%2FvwYj3zc3nD8cejapD3lMn%2Fqdp3pDHvFna3UWag9nmcuMeShRA%2BYpBGIFk1d3QJmg19%2FEKJMULw8c2u8ZH3EBL499szPsjd%2BTQ%2BPf1U5qax78ix%2BZwCLTTMYEiFcifx9wNvThVY2A4lOnba6odn%2BXdMWtkiXipdDAxBtcaCD2mlXiLp0axiRTrzHiJVo%2BbSKH3Zq0RQ5a3JN5PytqTVnWWCPu%2F6WlAsJDZru%2BC4JrXXPmeF79GR%2BVnajB3KSBXOf0jFdbPDTkypNzDe26uV8LC7rxvNFsKDZ2J7x1V9b2dBpQUL9T5xt1uCevLWgK3pLGPYqrW7hq4PF%2BQMYqVK3oZo4iIAHC1XbAXgX%2BYB%2BjZXQJMPoAwRCQe0v40csoO4JwlJgbgEQZ3KPJ54ilOHvYmfrMxxDPaTZNI4WeZQXm5hFVqMrmE1ZPQ0S27iI6myGc2xTbSdrzj%2FteHNhqZ3e8bFe%2BXatDvCZoeTv3pNPwn7zhqBb56wn%2B7o6kVwn%2BdBrtlH5bt8Lq7hJDHlWF3GQPczYgdoFzEYFsGxWhzf4wSFL2dSEeDDkkxAO7fMpA8%2FJ0AAheIX%2FqsWV8a4o4bjO7RYvZvVJIEt%2Byf0Ziz%2FwE%3D%3C%2Fdiagram%3E%3Cdiagram%20id%3D%224Df1BHetfkM0r4G3VRL4%22%20name%3D%22Vendor%22%3E7Vtbd9o4EP41PJJj%2BQZ%2BTEjSdLfZTcKetumbawujrbBYWdzy61eyZXyRuKTYQNrAObE1utjM981oNFI61mCy%2FED96fiehBB3TCNcdqzrjmmahmnzi5CsMonT9zJBRFGYiUAhGKIXKIWGlM5QCJNKQ0YIZmhaFQYkjmHAKjKfUrKoNhsRXH3q1I%2BgIhgGPlalX1DIxpm07xiF%2FA6iaJw%2FGRiyZuLnjaUgGfshWZRE1k3HGlBCWHY3WQ4gFsrL9ZL1u91Qu34xCmO2T4ePn%2F68C18eX%2B7vnv%2B6fbSil%2Bk31JXoJGyV%2F2BKZnEIRR%2BjY10RysYkIrGPPxEy5ULAhf9CxlYSKn%2FGCBeN2QTLWrhE7Gvp%2FlkMdeHI0vVSjpwWVrKQvQUMa1gkZEYDKfrD6nXND6vn7qOX4G%2B3qyWKv3YtyQifRpBt%2BZnAU7UF1hhw8kIygYyueBMKsc%2FQvPoivmRRtG5XKJrfSF2%2FQu9u83pvXYe9M9OhxHTu45l8UvNKHZGYyUpgyvKAYELT8S0j%2FRxB%2BbkbPRvlA7Bb%2B0IdQ1mMScwvV60CIp%2BROyDjwut5FSdk9t2tbkgUHiBFXEWQHsk1me65IWueHllLj2zrWJybiwP2W8Nit45bmIpl1weC%2BIimIYNP25KRVx565qFZPkTGG9mrhtT6NfYCT8u6M8BuiwNT9F%2B1Iz0dHRXkzQZ3MqNxFMV%2FhnHIyVtXPw%2FJp6kSAyaofbUYIwaHUz9VwoIvaGqaRRiXJv%2BRI75cnjBKfsBSjZt%2BeE1E%2FRDBSsjwPf3yOh%2BjKOaygNeL2aYCnJeX5cvmsy2kDC6346iqPbcHu2oPpifLi2JhkzcZl9Y0ttEWUK4C1E2IhAUPx5zspnENmY9wopoNxnz9B3cjpug4houbks11etw83P9mYg12VRjjWtSxLkv1MUNs9ZRymMQ3mtbmoCgk3EjYpViBbhgutXd9X87Wn%2ByZwGgi6FDuKJbSpSbBjM65f6m06PSu%2BR2jEN7yBTKKI6k%2FIbkn80LQAA1Bv0pDYNgqDwHQEBHUHXhzTOwpTLwMApgkabqB%2F%2FmHEMFDA8XpSl6w852TZ8LJst90tnE0IBj7HKPNGZTtzO2CKnNdS0NcnQcFVmvE7SvEHZCJ%2BEnCi%2FoYCtL6PHxYJejdj54PZxvwo12zRkdHM58DR0dH22mLjmpOZkChzwQbxch8SieLGBM%2FLNHzCU55mPtOzrMh594OdX%2ByerVJ3wX7us7Wok9TzWB9RnDx7jfPmZpN%2BM11GCm52N97Gm%2BPi5Yaf4bh2mk%2BwQmZCx%2F6kcGJYOaIkgm%2FfPFZMO5ilBzgPRvQqNPbJ6I3jxrRm7rsi4sF4UI0r%2BgqJ6Jwe90k9Xuc7AawpstUPwXR3UhcazNatmTNhuaSdPSsYVMPLMOsf87Pgq%2FL8%2BW%2ByWiGHH0laHZUblg6bphtRSmmmiDKFSsUsBdW5iZyjGHwgzf4m4aQlkx1MEsYf30hyp70ndZpwn9L9vjGUa3mrW7TT%2Bc1eSuZm6zTI292jSgMxKSUNqUC1kaoU0tY9XVBg6ujjtOaW1FTVhUrz6CTccQTnPObZA%2FnkInIqAg%2BtpCkHcsvcSSEI3%2BGWRMMaSJ0zHdlJAtsG%2By7zGmNBZp0kW66fqAknAWs5AZEYjNpaOY%2Bmpk3AKJb24vp9bw9IwTQGoi68wNtzAL8eseBJuKd36qnb4AC4KQU0G5TOarmW9iQ4%2Fqhq%2BxAgpMXn%2BVwaaE4jJCW8tMI9Y284lyDsz7HkJ1r8Pq9TkPnGnZsCx62vX7otuCGfd7a8sMxa3xpeZ9XnQyOQit9lqYtQLXt3APxPMh4c6%2FwBqz3dfDsPol3qN432JFTs6Mjn5cAv6LdbEk9nsxwrGMbjgFAxXQuLGDvMJ%2B0VJ%2BzzgE656TQHTliqcHmvNLnFRGLkQG%2BjlhsMz%2BZedYRS7a92rintbyqp7Xr%2BYqWPa2abR4edKRBObnU6EGp6jmoRtYidm0LYF0%2B3VpETSxp88ylnMJvi5bXJlq8WPxPTmZwxX82WTf%2FAw%3D%3D%3C%2Fdiagram%3E%3C%2Fmxfile%3E)
























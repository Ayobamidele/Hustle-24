# from django.contrib.auth import get_user_model
# from django.test import TestCase

# User = get_user_model()

# class LogInTest(TestCase):
#     def setUp(self):
#         self.credentials = {
#             'username': 'test user',
#             'email': 'testuser@example.com',
#             'first_name' :'test',
# 			'last_name': 'user',
#             'is_vendor': True,
#             'is_customer': True,
#             'password': 'secret'}
#         User.objects.create_user(**self.credentials)
#     def test_login(self):
#         # send login data
#         response = self.client.post('/login/', self.credentials, follow=True)
#         # should be logged in now
#         # print(response.context)
#         print(self.assertTrue(response.context['user'].is_active))
# /home/bami/snap/postman/182/Postman/files
import requests
# /home/bami/Documents/Bami/src/Hustle_24/static/3512318_White_Black.png

        # \          SORRY            /
        #  \                         /
        #   \    This page does     /
        #    ]   not exist yet.    [    ,'|
        #    ]                     [   /  |
        #    ]___               ___[ ,'   |
        #    ]  ]\             /[  [ |:   |
        #    ]  ] \           / [  [ |:   |
        #    ]  ]  ]         [  [  [ |:   |
        #    ]  ]  ]__     __[  [  [ |:   |
        #    ]  ]  ] ]\ _ /[ [  [  [ |:   |
        #    ]  ]  ] ] (#) [ [  [  [ :===='
        #    ]  ]  ]_].nHn.[_[  [  [
        #    ]  ]  ]  HHHHH. [  [  [
        #    ]  ] /   `HH("N  \ [  [
        #    ]__]/     HHH  "  \[__[
        #    ]         NNN         [
        #    ]         N/"         [
        #    ]         N H         [
        #   /          N            \
        #  /           q,            \
        # /                           \

url = 'http://127.0.0.1:8000/api/Product-photos/'

files=[
        ('image',('3512318_White_Black.png',open('static/3512318_White_Black.png','rb'),'image/png'))
]

data = {
    "title": "Addidas NGx32344 Street Edition",
    "regular_price": 290.63,
    "discount_price": 250.99,
    "description": "White Street Edition",
    "stock": 29,
    "category": [
                    {
                        "name": "Shoe",
                        "slug": "Shoe"
                    },
                    {
                        "name": "Addidas",
                        "slug": "Addidas"
                    }
                ]
}
data = {
    "image": "/home/bami/Documents/Bami/src/Hustle_24/static/3512318_White_Black.png",
    "alt_text": "shoe (1)",
    "is_feature": False,
    "product": 1
}

response = requests.post(url, data=data)
print(response, response)
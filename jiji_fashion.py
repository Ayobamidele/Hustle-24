import requests
import json
import os
from fake_useragent import UserAgent
import time

ua = UserAgent()
headers = {'User-Agent':str(ua.random)}
page = 1
product_count = 0
status = True
category = "fashion-and-beauty"
request = requests.Session()
product_list = []


def get_attrs(attrs):
	try:
		return next(item for item in item_info['advert']['attrs'] if item["name"] == attrs)['value']
	except Exception as e:
		return ""


def get_fav(data):
	try:
		return item_info['advert']['fav_count']
	except Exception as e:
		return ""



def get_product_details(guid, id):
	headers = {"User-Agent": str(ua.random)}
	try:
		url = f"https://jiji.ng/api_web/v1/item/{guid}"
		response = requests.get(url, headers=headers)
	except Exception as e:
		url = 'https://jiji.ng/api_web/v1/item/' + str(id)
		response = requests.get(url, headers=headers)

	try:
		item_info = response.json()
		condition = get_attrs("Condition")
		brand = get_attrs("Brand")
		fav_count = get_fav(item_info)
		gender = get_attrs("Gender")
		return {'condition': "new" if condition == "Brand New" else "used", "brand": brand, "fav_count": fav_count}
	except Exception as e:
		print(item_info)
		return {'condition': "used", "brand": "", "fav_count": ""}


def update_record(file):
	with open(file, "w") as final:
		json.dump(product_list, final, indent=4)


while status:
	url = f'https://jiji.ng/api_web/v1/listing?slug={category}&webp=true&page={page}'
	response = request.get(url, headers=headers)
	if response.status_code == 200 and response.json():
		response_data = response.json()
		for product in response_data['adverts_list']['adverts']:
			product_count += 1
			product_attrs = get_product_details(product.get('guid'), product.get('id'))
			product_data = {
			"id": product_count,
			"title": product['title'],
			"description": product['short_description'],
			"availability": "available for order" if product['status'] == "active" else "discontinued",
			"condition": product_attrs['condition'],
			"price": "{:.2f}".format(product['price_obj']['value']) + " NGN",
			"link": "https://jiji.ng" + product['url'],
			"image_link": product['image_obj']['url'],
			"brand": product_attrs['brand'],
			"google_product_category": "Apparel & Accessories > Clothing",
			"fb_product_category": "Clothing & Accessories > Clothing",
			"quantity_to_sell_on_facebook": product_attrs['fav_count'],
			"sale_price": "{:.2f}".format(product['price_obj']['value']) + " NGN",
			"sale_price_effective_date": "",
			"item_group_id": "",
			"gender": product_attrs['fav_count'],
			"color": "",
			"size": "",
			"age_group": "",
			"material": "",
			"pattern": "",
			"shipping": "",
			"shipping_weight": "",
			}
			product_list.append(product_data)
			update_record("fashion-and-beauty.json")
			print(product_count,".    ", product_data, "page" ,page)
	page += 1





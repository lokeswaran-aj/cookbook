from typing import List, TypedDict

import requests


class OrderItem(TypedDict):
    """Individual menu item in an order"""

    itemName: str
    quantity: int


class OrderRequest(TypedDict):
    """Complete order request structure expected by the API"""

    menuDTO: List[OrderItem]


def fetch_restaurants_by_location(location: str) -> list[dict]:
    url = "https://fakerestaurantapi.runasp.net/api/Restaurant"
    params = {"address": location}

    response = requests.get(url, params=params)
    data = response.json()
    return data


def fetch_menu_by_restaurant_id(restaurant_id: str) -> list[dict]:
    url = f"https://fakerestaurantapi.runasp.net/api/Restaurant/{restaurant_id}/menu"
    response = requests.get(url)
    data = response.json()
    return data


def register_new_user(user_email: str, password: str) -> dict:
    url = "https://fakerestaurantapi.runasp.net/api/User/register"
    data = {"userEmail": user_email, "password": password}
    response = requests.post(url, json=data)
    return response.json()


def get_api_key(user_email: str, password: str) -> dict:
    url = "https://fakerestaurantapi.runasp.net/api/User/getusercode"
    params = {"userEmail": user_email, "password": password}
    response = requests.get(url, params=params)
    return response.json()


def place_an_order(restaurant_id: str, api_key: str, order_items: OrderRequest) -> dict:
    url = f"https://fakerestaurantapi.runasp.net/api/Order/{restaurant_id}/makeorder?apikey={api_key}"
    response = requests.post(url, json=order_items)
    return response.json()


def get_order_status(master_id: str, api_key: str) -> dict:
    url = f"https://fakerestaurantapi.runasp.net/api/Order/{master_id}?apikey={api_key}"
    response = requests.get(url)
    return response.json()

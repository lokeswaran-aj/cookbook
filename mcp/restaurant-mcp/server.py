from api import OrderItem, fetch_menu_by_restaurant_id, fetch_restaurants_by_location
from api import get_api_key as api_get_api_key
from api import get_order_status as api_get_order_status
from api import place_an_order as api_place_an_order
from api import register_new_user as api_register_new_user
from fastmcp import FastMCP
from fastmcp.prompts.prompt import PromptMessage, TextContent

mcp = FastMCP("restaurant-mcp")


@mcp.resource(uri="https://get-restaurants", name="Get Restaurants")
def list_restaurants() -> list[dict]:
    """Get information about a restaurant"""
    return fetch_restaurants_by_location("bangalore")


@mcp.resource("https://get-menu/?restaurant_id={restaurant_id}", name="Get Menu")
def list_menu_by_restaurant_id(restaurant_id: str) -> list[dict]:
    """Get information about a menu"""
    return fetch_menu_by_restaurant_id(restaurant_id)


@mcp.tool(name="get_restaurants")
def get_restaurants(location: str) -> list[dict]:
    """Get information about a restaurant"""
    return fetch_restaurants_by_location(location)


@mcp.tool(name="get_menu")
def get_menu(restaurant_id: str) -> list[dict]:
    """Get information about a menu"""
    return fetch_menu_by_restaurant_id(restaurant_id)


@mcp.tool(name="register_new_user", enabled=False)
def register_new_user(user_email: str, password: str) -> dict:
    """Register a new user"""
    return api_register_new_user(user_email, password)


@mcp.tool(name="get_api_key")
def get_api_key(user_email: str, password: str) -> dict:
    """Get API key"""
    return api_get_api_key(user_email, password)


@mcp.tool(name="place_an_order")
def place_an_order(
    restaurant_id: str, api_key: str, order_items: list[OrderItem]
) -> dict:
    """Place an order"""
    formatted_order = {"menuDTO": order_items}
    return api_place_an_order(restaurant_id, api_key, formatted_order)


@mcp.tool(name="get_order_status")
def get_order_status(master_id: str, api_key: str) -> dict:
    """Get the status of an order"""
    return api_get_order_status(master_id, api_key)


@mcp.prompt
def place_pizza_margherita_from_toit_brewery(quantity: int) -> str:
    """Place an order for a pizza margherita from Toit Brewery"""
    content = f"I want to order {quantity} pizza margherita from Toit Brewery"
    return PromptMessage(role="user", content=TextContent(type="text", text=content))


if __name__ == "__main__":
    mcp.run()

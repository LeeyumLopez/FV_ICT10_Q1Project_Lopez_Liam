from pyscript import display

# SW2/main.py
# This file contains simple restaurant metadata and a menu list used by the
# `SW2/index.html` page. The values here are read by the page's PyScript code
# to populate the UI (restaurant name, owner, year established, and menu items).
#
# Notes:
# - Prices are represented as numbers (treated as PHP currency in the UI).
# - This module currently only holds data; presentation and DOM updates are
#   handled in the HTML page's PyScript blocks which import or reference this file.

# Restaurant metadata
restaurant_name = "ARRGHH Resto"  # visible in the hero/header

owner_name = "Liam G. Lopez"      # restaurant owner

year_established = "10 BCE"        # fun example value for the establishment year

# Menu: list of dicts with `name` and `price` keys. Prices are integers (₱).
list_of_menu_items = [
    {"name": "Goo Spaghetti", "price": 150},
    {"name": "Livechicken Burger", "price": 250},
    {"name": "Chocolate Milkshake", "price": 120},
    {"name": "Human Salad", "price": 130},
    {"name": "Toe Fries", "price": 75}
]


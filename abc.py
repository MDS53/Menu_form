from flask import Flask, request, render_template

app = Flask(__name__)

# Sample menu items with prices
menu1 = {
    "Garlic Bread": {
        "price": 5,
        "image": "https://wallpaperaccess.com/full/1972917.jpg"  # Example image URL for Garlic Bread
    },
    "Caprese Salad": {
        "price": 8,
        "image": "https://wallpaperaccess.com/full/1972917.jpg"  # Example image URL for Caprese Salad,
    }
}

menu2={
   "Pizza": {
        "price": 12,
        "image": "https://wallpaperaccess.com/full/1972917.jpg"  # Example image URL for Pizza
    },
    "Pasta": {
        "price": 10,
        "image": "https://wallpaperaccess.com/full/1972917.jpg"  # Example image URL for Pasta
    }}

menu3={
   "Coke": {
        "price": 2,
        "image": "https://wallpaperaccess.com/full/1972917.jpg"  # Example image URL for Coke
    },
    "Pepsi": {
        "price": 2,
        "image": "https://wallpaperaccess.com/full/1972917.jpg"  # Example image URL for Pepsi
    },
    "Lemonade": {
        "price": 3,
        "image": "https://wallpaperaccess.com/full/1972917.jpg"  # Example image URL for Lemonade
    }
}


menu={**menu1,**menu2,**menu3}
print(menu)
print(menu['Garlic Bread']['price'])
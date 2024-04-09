from flask import Flask, request, render_template
import random 

app = Flask(__name__)

# Sample menu items with prices
menu1 = {
    "Chicken curry": {
        "price": 8,
        "image": "https://i.pinimg.com/originals/62/5f/af/625fafa487289e76bd3f599bd2a25b55.jpg", # Example image URL for Garlic Bread
        "ingredients" : "kaju toppups, chicken curry in a bowl,lemon slices(2),onion slices(2)"
    },
    "Mutton Curry": {
        "price": 15,
        "image": "https://www.whiskaffair.com/wp-content/uploads/2019/04/Punjabi-Mutton-Curry-1.jpg"  # Example image URL for Caprese Salad,
    },
    "Mutton kheema curry": {
        "price": 13,
        "image": "https://www.indianhealthyrecipes.com/wp-content/uploads/2018/08/mutton-keema-recipe-500x375.jpg"  # Example image URL for Caprese Salad,
    },
    "Chicken pakodi": {
        "price": 10,
        "image": "https://vismaifood.com/storage/app/uploads/public/ef5/cc0/637/thumb__1200_0_0_0_auto.jpg"  # Example image URL for Garlic Bread
    },
}

menu2={
   "Special Chicken Biriyani": {
        "price": 12,
        "image": "https://th.bing.com/th/id/OIP.QpZ4aBKAKSS82vj0YAhjpAHaFj?rs=1&pid=ImgDetMain"  # Example image URL for Pizza
    },
    "Chicken Dum Biriyani": {
        "price": 10,
        "image": "https://insurancesites.sgp1.digitaloceanspaces.com/wp-content/uploads/sites/156/2021/05/18063006/chickenBiryani-600x600.jpeg"  # Example image URL for Pasta
    },
    "Mutton Biriyani": {
        "price": 10,
        "image": "https://spiceeats.com/wp-content/uploads/2020/07/Mutton-Biryani.jpg"  # Example image URL for Pasta
    },
    "Mutton Dum Biriyani": {
        "price": 10,
        "image": "https://anantha.in/wp-content/uploads/2020/03/Mutton-Biryani-Img.jpg"  # Example image URL for Pasta
    },
    "Chicken fry Biryani": {
        "price": 10,
        "image": "https://lh5.googleusercontent.com/proxy/996ZU-ziqwxG-XNN0UyxRXTmjTVFFQUEOfNCxHCf6-vdHHMaLXsI_baxR6_24rcNBY8TewjIt7Z2uhkgAgQQf6xxtX6gETSElIdt60Zpw3ACQy1AZ5irR8XlxC9GiLNmZLLCs3Ud5oLiLbm8T6Wk=s0-d"  # Example image URL for Pasta
    }
}

menu3={
   "Coke": {
        "price": 2,
        "image": "https://th.bing.com/th/id/OIP.r5YDp81DKs5tkvBpo1JwaAHaLb?rs=1&pid=ImgDetMain"  # Example image URL for Coke
    },
    "Pepsi": {
        "price": 2,
        "image": "https://th.bing.com/th/id/OIP._Q1khAeYkZfCO4Wm-6RGwwHaLH?rs=1&pid=ImgDetMain"  # Example image URL for Pepsi
    },
    "Lemonade": {
        "price": 3,
        "image": "https://th.bing.com/th/id/OIP.gw5NnhT8vP-vKVg6syXKygAAAA?rs=1&pid=ImgDetMain"  # Example image URL for Lemonade
    }
}


menu={**menu1,**menu2,**menu3}

@app.route('/')
def menu_form():
    a=["“Our secret ingredient is love, but don’t tell anyone. Order now!”",
"“Life is too short for average food. Try our specials!”",
"“You don’t need silverware to eat good food. Try our finger-licking dishes!”",
"“We serve happiness on a plate. Come, have a taste!”",
"“Our food is like a hug on a plate. Order your hug now!”",
"“Good food is good mood. Boost your mood with our menu!”",
"“We don’t just serve food, we serve memories. Create yours today!”",
"“Eat well, live simply, laugh often. Start with our menu!”",
"Remember, a meal at a restaurant is more than just food, it’s an experience! 😊" ]
    
    
    return render_template('menu_form.html', menu1=menu1,menu2=menu2,menu3=menu3,menu=menu,quotes=random.choice(a))

@app.route('/bill', methods=['POST'])
def generate_bill():
    starters_quantity = {}
    main_course_quantity = {}
    drinks_quantity={}

    for item, price in menu.items():
        starters_quantity[item] = int(request.form.get(f'starters_quantity[{item}]', 0))
        main_course_quantity[item] = int(request.form.get(f'main_course_quantity[{item}]', 0))
        drinks_quantity[item] = int(request.form.get(f'drinks_quantity[{item}]', 0))

    """selected_drinks = request.form.get('drinks')
    drinks_quantity = int(request.form.get('drinks_quantity', 0))"""
    
    print(starters_quantity)
    print("*"*100)
    print(main_course_quantity)
    print("*"*100)
    #print(selected_drinks)
    print(drinks_quantity)
    

    total_cost = 0
    items_ordered = []

    for item, quantity in starters_quantity.items():
        if item in ["Chicken curry","Mutton Curry","Chicken pakodi","Mutton kheema curry"]:
            if quantity > 0:
                total_cost += menu1[item]['price'] * quantity
                items_ordered.append(f"{quantity} x {item}")

    for item, quantity in main_course_quantity.items():
        if item in ["Special Chicken Biriyani","Chicken Biriyani","Chicken Dum Biriyani","Mutton Biriyani","Mutton Dum Biriyani","Chicken fry Biryani"]:
            if quantity > 0:
                total_cost += menu2[item]['price'] * quantity
                items_ordered.append(f"{quantity} x {item}")

    for item, quantity in drinks_quantity.items():
        if item in ["Coke","Pepsi","Lemonade"]:
            if quantity > 0:
                total_cost += menu3[item]['price'] * quantity
                items_ordered.append(f"{quantity} x {item}")

    return render_template('bill.html', items=items_ordered, total=total_cost)

if __name__ == '__main__':
    app.run(debug=True)

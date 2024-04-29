import pandas as pd
import random


random.seed(42)



product_groups = [
    ["Laptop", "Laptop Bag", "Wireless Mouse", "USB-C Adapter"],
    ["Smartphone", "Phone Case", "Screen Protector", "Portable Charger"],
    ["Backpack", "Water Bottle", "Lunch Box", "Thermal Flask"],
    ["Running Shoes", "Athletic Socks", "Gym Shorts", "Sweatband"],
    ["Book", "Bookmark", "Reading Light", "Eye Glasses"],
    ["Camera", "Camera Bag", "Tripod", "SD Card"],
    ["Gardening Gloves", "Pruning Shears", "Plant Pots", "Watering Can"],
    ["Board Game", "Playing Cards", "Dice Set", "Puzzle"],
    ["Yoga Mat", "Yoga Pants", "Resistance Bands", "Water Bottle"],
    ["Grill", "Charcoal", "Grill Tools Set", "Apron"]
]




def random_basket(group):
    num_products = random.randint(1, len(group))
    return random.sample(group, num_products)




num_users = 35
data = {'user_id': range(1, num_users + 1),
        'basket': [random_basket(random.choice(product_groups)) for _ in range(num_users)]}




df = pd.DataFrame(data)



print(df)





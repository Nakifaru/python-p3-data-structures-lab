spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food['name'] for food in spicy_foods]
    pass

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food['heat_level'] >= 5]
    pass

def print_spicy_foods(spicy_foods):
    def emojis(num):
        return '🌶' * num
    for food in spicy_foods:
        name = food['name']
        cuisine = food['cuisine']
        emojis_shown = emojis(food['heat_level'])
        print(f'{name} ({cuisine}) | Heat Level: {emojis_shown}')
    pass

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        while food['cuisine'] == cuisine:
            return food 
    # return [food for food in spicy_foods if food['cuisine'] == cuisine]
    pass

def print_spiciest_foods(spicy_foods):
    def emojis(num):
        return '🌶' * num
    for food in spicy_foods:
        if food['heat_level'] > 5:
            name = food['name']
            cuisine = food['cuisine']
            emojis_shown = emojis(food['heat_level'])
            print(f'{name} ({cuisine}) | Heat Level: {emojis_shown}')
    pass

def get_average_heat_level(spicy_foods):
    total_heat_level = 0
    for food in spicy_foods:
        total_heat_level += food['heat_level']
    average_heat_level = total_heat_level / len(spicy_foods)
    return average_heat_level
    pass

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
    pass

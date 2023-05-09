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
    return [foods["name"] for foods in spicy_foods]


def get_spiciest_foods(spicy_foods):
    return [foods for foods in spicy_foods if foods["heat_level"] > 5]


def print_spicy_foods(spicy_foods):
    return [print(f"{foods['name']} ({foods['cuisine']}) | Heat Level: {foods['heat_level'] * '🌶'}") for foods in spicy_foods]
# cool lil pepper

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    food_list = [foods for foods in spicy_foods if foods["cuisine"] == cuisine]
    return food_list[0]


def print_spiciest_foods(spicy_foods):
    return print_spicy_foods(get_spiciest_foods(spicy_foods))


def get_average_heat_level(spicy_foods):
    
    return sum([foods["heat_level"] for foods in spicy_foods]) / len(spicy_foods)


def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

file_name = 'Recipes.txt'


def recipes_catalog(file_name):
    with open(file_name, encoding='utf-8') as file:
        recipes = {}
        for line in file:
            dish_name = line.strip()
            ingredients = []
            for item in range(int(file.readline())):
                ingredient = file.readline().strip().split('|')
                keys = ['ingredient_name', 'quantity', 'measure']
                ing_elements = dict(zip(keys, ingredient))
                ingredients.append(ing_elements)
            recipes[dish_name] = ingredients
            file.readline()
        return recipes


# print(recipes_catalog(file_name))


def get_shop_list_by_dishes(dishes, person_count):
    list_by_dishes = {}
    for dish, ingredients in recipes_catalog(file_name).items():
        if dish in dishes:
            for ingredient in ingredients:
                if ingredient['ingredient_name'] not in list_by_dishes:
                    list_by_dishes[ingredient.pop('ingredient_name')] = ingredient
                    ingredient['quantity'] = int(ingredient['quantity']) * person_count
                else:
                    list_by_dishes[ingredient.pop('ingredient_name')] = ingredient
                    ingredient['quantity'] = int(ingredient['quantity']) * person_count * len(dishes)

    return list_by_dishes


print(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2))

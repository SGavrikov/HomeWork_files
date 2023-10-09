
with open("Files/recipes.txt", encoding='utf-8') as f:
    cook_book = {}
    for line in f:
        meal_name = line[:-1]
        number_ingredient = int(f.readline())
        ingredient_dict = []
        for num in range(number_ingredient):
            ingredients_list = f.readline().replace('\n', '').split(' | ')
            ingredient_dict.append({'Ingredient_mame': ingredients_list[0],
                                    'quantity': ingredients_list[1], 'measure': ingredients_list[2]})
            cook_book[meal_name] = ingredient_dict
        f.readline()


def get_shop_list_by_dishes(dishes, person_count):
    ingredients = {}
    for meal in dishes:
        for elem in cook_book[meal]:
            if elem['Ingredient_mame'] in ingredients:
                ingredients[elem['Ingredient_mame']]['quantity'] += int(elem['quantity']) * person_count
            else:
                ingredients[elem['Ingredient_mame']] = {'measure': elem['measure'],
                                                        'quantity': int(elem['quantity'])*person_count}
    return ingredients


print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 3))

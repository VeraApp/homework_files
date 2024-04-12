cook_book = {}

def create_json():
    with open('resipes.txt', encoding='utf-8') as file:
        for line in file:
            name_dish = line.strip()
            count_ingredient = int(file.readline())
            list_ingredient = []
            list_ingredients = []
            for i in range(count_ingredient):
                str = file.readline()
                params = str.split(' | ')
                ingredients = {'ingredient_name': params[0], 'quantity': int(params[1]), 'measure': params[2]}
                list_ingredient.append(ingredients)
            #line.strip()
            list_ingredients = list_ingredient
            dish = {name_dish: list_ingredients}
            file.readline()
            cook_book.update(dish)
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    result_shop_list = {}
    for dish in dishes:
        if dish in cook_book.keys():
            for ingridient in cook_book[dish]:
                ingridient_name = ingridient['ingredient_name']
                measure = ingridient['measure']
                if ingridient_name in result_shop_list.keys():
                    sum_quanity = result_shop_list[ingridient_name]['quantity'] + ingridient['quantity'] * person_count
                else:
                    sum_quanity = ingridient['quantity'] * person_count
                json_ingridient =  {'measure': measure, 'quantity': sum_quanity}
                result_shop_list[ingridient_name] = json_ingridient
    return result_shop_list


cook_book = create_json()
print(cook_book)
dishes = ['Запеченный картофель', 'Омлет']
person_count = 2
result_list_shop = get_shop_list_by_dishes(dishes, person_count)
print(result_list_shop)

from pprint import pprint
cook_book = {}
with open('recipes.txt', encoding='utf-8') as file:
    key = ''
    for line in file:
        line = line.strip()
        if line.isdigit():
            continue
        elif line and '|' not in line:
            cook_book[line] = []
            key = line
        elif line and '|' in line:
            name, qt, msure = line.split(" | ")
            cook_book.get(key).append(dict(ingredient_name=name, quantity=int(qt), measure=msure))

def get_shop_list_by_dishes(dishes,person_count):
    dishe = []
    for i in cook_book.keys():
        dishe.append(i)
    shop_list = {}
    for d in dishes:
        if d not in dishe:
            return print('Нет такого блюда в базе данных')
        else:
            for id in dishes:
                for h in cook_book[id]:
                    keyy = h['ingredient_name']
                    meas,qul = h['measure'],h['quantity']*person_count
                    shop_list[keyy] = dict(measure=meas, quantity=qul)

            return pprint(shop_list)


get_shop_list_by_dishes(dishes=['Запеченный картофель', 'Омлет'],person_count=20)
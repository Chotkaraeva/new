
import json
import datetime



FILE_PATH = 'data.json'
def get_data(ge_price=None, le_price=None, s_status = 'sold', i_status = 'in_stock', date_c = '2022-10-08 18:36:51.674564'):
    with open(FILE_PATH) as file:
        data = json.load(file)
    if ge_price:
        new_data = [i for i in data if i ['price'] >= ge_price ]
        return new_data
    if le_price:
        new_data = [i for i in data if i ['price'] <= le_price ]
        return new_data
    if s_status:
        new_data = [i for i in data if i ['status'] == s_status ]
        return new_data
    if i_status:
        new_data = [i for i in data if i ['status'] == i_status ]
        return new_data
    if date_c:
        new_data = [i for i in data if i ['creation_date'] == '2022-10-08 18:36:51.674564']
        return new_data
    return data
        
def get_one_data(id):
    data = get_data()
    one_data = [i for i in data if i['id'] == id]
    if one_data:
        return one_data[0]
    return "Нет такого товара!"

def post_data():
    data = get_data()
    max_id = max([i['id'] for i in data])
    data.append({
        'id' : max_id + 1,
        'name': input("Введите имя нового товара: "),
        'price': float(input("Ведите цену нового товара: ")),
        'creation_date' : str(datetime.datetime.now()),
        'date_of_update' : str(datetime.datetime.now()),
        'description' : input("Введите описание нового товара: "),
        'status' : input('Введите "in_stock" если товар в наличии и "sold" если продан: '),
    })
    with open(FILE_PATH, 'w') as file:
        json.dump(data, file)

    return "created"

def update_data(id):
    data = get_data()
    data_update = [i for i in data if i['id'] == id]

    if data_update:
        index_ = data.index(data_update[0])
        if input('Хотите обновить имя?(да/нет): ') == 'да':
            data[index_]['name'] = input('Введите новое имя: ')
        if input('Хотите обновить цену?(да/нет): ') == 'да':
            data[index_]['price'] = float(input('Введите новую цену: '))
        
        data[index_]['date_of_update'] = str(datetime.datetime.now())
        if input('Хотите обновить описание?(да/нет): ') == 'да':
            data[index_]['description'] = input('Введите описание нового товара: ')
        data[index_]['status'] = input('Введите "in_stock" если товар в наличии и "sold" если продан: ')
        json.dump(data, open(FILE_PATH, 'w'))
        return 'updated'
    return "Нет такого товара!"



def delete_data(id):
    data = get_data()
    data_delete = [i for i in data if i['id'] == id]
    if delete_data:
        data.remove(data_delete[0])
        json.dump(data, open('FILE_PATH', 'w'))
        return "Deleted!!!"
    return "Нет такого товара!"



# print(get_data(s_status = 'sold'))


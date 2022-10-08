from views import *

def main():
    while True:
        print('Привет вот функционал: \n1 - получить все товары \n2 - получить определенный товар \n3 - создать товар \n4 - удалить товар \n5 - обновить товар')
        method = input('Введи число: ')
        if method == '1':
            print(get_data())
        elif method == '2':
            id = int(input('Введи id товара: '))
            print(get_one_data(id))
        elif method == '3':
            print(post_data())
        elif method == '4':
            id = int(input('Введите id товара который хотите удалить: '))
            print(delete_data(id))
        elif method == '5':
            id = int(input('Введите id товара который хотите обновить: '))
            print(update_data(id))
        else:
            print('Нет такого функционала!')


if __name__ == '__main__':
    main()
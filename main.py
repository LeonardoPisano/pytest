#!/usr/local/bin/python3.6
import xml.dom.minidom as md   #Стандартная поставка в python

import Client
import Product
import Sale

def main():
    # Читаем XML файл с начальными данными в DOM дерево
    domtree = md.parse("shop.xml")      #parse - разбираем файл
    domtree.normalize()

    # Берём корневой элемент документа
    rootnode = domtree.getElementsByTagName("shop")[0]      #Обращаемся к первому файлу с этим именем

    # Забираем группы clients, products и sales из XML
    clients = rootnode.getElementsByTagName("clients")[0].getElementsByTagName('client')
    for client in clients:
        client_obj = Client.client(client.getAttribute('surname'),
            client.getAttribute('name'),
            client.getAttribute('secname'),
            client.getAttribute('address'),
            client.getAttribute('phone'),
            client.getAttribute('email'), 
            client.getAttribute('permanent'))
        print('Зарегистрированные клиенты: {}, {}, {}'.format(client_obj.getSurname(),client_obj.getName(),client_obj.getSecname()))

    products = rootnode.getElementsByTagName("products")[0].getElementsByTagName('product')

    sales = rootnode.getElementsByTagName("sales")[0].getElementsByTagName('sales')

    # Собрать список продуктов

    # Собрать список продаж

if __name__ == '__main__':
    main()


#!/usr/bin/python3.6
import fileinput

import Client
import Product
import Sale

class repl:
    __client_attributes = []
    __product_attributes = []
    __sale_attributes = []

    __clients = dict()
    __products = dict()
    __sales = dict()

    __finput = fileinput.FileInput()

    def __init__(self,
        clients,
        products,
        sales,
        client_attributes,
        product_attributes,
        sale_attributes):
        self.__clients = clients
        self.__products = products
        self.__sales = sales
        self.__client_attributes = client_attributes
        self.__product_attributes = product_attributes
        self.__sale_attributes = sale_attributes

    def print(self):
    #'''
    #from pprint import pprint
    #pprint(actors) 
    #Печать содержимого словарей, объектов, как оно видится в коде
    #'''
    # Печатаем на stdout(Стандартные потоки ввода-вывода) то, что наконструировали.
        for client_key, client_value in self.__clients.items():  #обходим список клиентов (перебор) 
            print('Зарегистрированные клиенты: {} {} {}'.format(client_value.getSurname(),
                client_value.getName(),
                client_value.getSecname()))

        # Печатаем на stdout то, что нашли.
        for product_key, product_value in self.__products.items():
            print('Продукт в наличии: {}, {} руб., ед. изм.: {}'.format(product_value.getDesignation(),
                product_value.getPrice(),
                product_value.getUnit()))

        for sale_key, sale_value in self.__sales.items():
            print('Продажа: {} от {}, доставка {} клиенту {}, в колличесстве: {}'.format
                (sale_value.getProduct().getDesignation(),
                 sale_value.getDatsale(),
                 sale_value.getDatdelivery(),
                 sale_value.getClient().getName(),
                 sale_value.getNumber()))

    def sale_info(self, id):
            return 'Продажа продукта {}  Клиенту: {} ,{} \n'.format(id, self.__sales[id].getClient().getName(),
            self.__sales[id].getPproduct().getDdesignation(),
            self.__sales[id].getDatsale())
    def reader(self):
        for line in self.__finput:
            if line.startswith('stop'):
                print('Stopping')
                return
            if line.startswith('print'):
                self.print()
                continue
            if line.startswith('new client'):
                properties = self.__read_properties(self.__client_attributes)
                client_obj = Clients.clients(properties)
                self.__clients[' '] = client_obj
                continue
            if line.startswith('new product'):
                print('Adding new product')
                continue
            if line.startswith('new sale'):
                print('Adding new sale')
                continue
            if line.startswith('del client'):
                print('Deleting client')
                continue
            if line.startswith('del product'):
                print('Deleting product')
                continue
            if line.startswith('del sale'):
                print('Deleting sale')
                continue
            print('Invalid command given: {}'.format(line))

    def __read_properties(self, properties):
        finput = fileinput.FileInput()
        obj = dict()
        for prop in properties:
            obj[prop] = input('Input value for property: {}'.format(prop))
        return obj

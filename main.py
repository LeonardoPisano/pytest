#!/usr/bin/python3.6
import xml.dom.minidom as md   #Стандартная поставка в python
import argparse     #модуль для обработки аргументов командной строки
import sys          #предоставляет системе особые параметры и функции

import Client
import Product
import Sale

import Parser          # Модуль чтения и записи XML.

import Database        # Модуль чтения и записи БД SQLite3

class runner:
    __client_attributes = ('name',
        'surname',
        'secname',
        'address',
        'phone',
        'email',
        'permanent',
        'id')
    __product_attributes = ('designation',
        'price',
        'unit',
        'id')
    __sales_attributes = ('product',
        'client',
        'datsale',
        'datdelivery',
        'number')
    __source_path = ''
    __clients = dict()
    __products = dict()
    __sales = dict()


    def run_from_xml(self, source, rootnode):
        shop_xml = Parser.parser(source, rootnode)

        # Получаем список словарей-клиентов.
        # Каждый клиент это набор свойств одного клиента.
        clients = shop_xml.get_entries(self.__client_attributes,        #список словарей.
            'clients',
            'client')
        # Конструируем объекты клиентов из словарей и мапим айдишники
        # клиентов в объекты клиентов. Это понадобится, чтобы связать
        # айдишники клиентов с продажами.
        for client in clients:
            client_obj = Client.client(client)                      #обходим конкретные атрибуты определенного клиента
            self.__clients[client_obj.getID()] = client_obj         #соотносим конкретному клиенту ID

        # Печатаем на stdout(Стандартные потоки ввода-вывода) то, что наконструировали.
        for client_key, client_value in self.__clients.items():  #обходим список клиентов (перебор) 
            print('Зарегистрированные клиенты: {} {} {}'.format(client_value.getSurname(),
                client_value.getName(),
                client_value.getSecname()))

        #from pprint import pprint
        #pprint(clients)

        # Здесь мы получаем список словарей-продуктов
        # Каждый словарь это набор свойств одного продукта.
        products = shop_xml.get_entries(self.__product_attributes,
            'products',
            'product')
        # Мапим айдишники продуктов в объекты продуктов. Это нужно
        # для связи продаж с продуктами.
        for product in products:
            product_obj = Product.product(product)
            self.__products[product_obj.getID()] = product_obj

        # Печатаем на stdout то, что нашли.
        for product_key, product_value in self.__products.items():
            print('Продукт в наличии: {}, {} руб., ед. изм.: {}'.format(product_value.getDesignation(),
                product_value.getPrice(),
                product_value.getUnit()))

        # Наконец, собираем список словарей продаж.
        sales = shop_xml.get_entries(self.__sales_attributes,
            'sales',
            'sale')

        #Конструируем объекты продаж, мапим их номера в объекты,
        #заодно подтягиваем айдишники клиентов.
        for sale in sales:
            if sale['product'] in self.__products.keys() and sale['client'] in self.__clients.keys():
                sale_obj = Sale.sale(sale, self.__products, self.__clients)
                self.__sales[sale_obj.getNumber()] = sale_obj
                print (sale_obj)
            else:
                print ('sorry')
        for sale_key, sale_value in self.__sales.items():
            print('Продажа: {} от {}, доставка {} клиенту {}, в колличесстве: {}'.format
                (sale_value.getProduct().getDesignation(),
                 sale_value.getDatsale(),
                 sale_value.getDatdelivery(),
                 sale_value.getClient().getName(),
                 sale_value.getNumber()))

    def run_from_sqlite(self, dbfile='shop.sqlite3'):
        '''
        Прочитать данные для работы из базы данных SQLite3.
        '''
        print('Run from sqlite')

    def save_to_xml(self, xmlfile='new.xml'):
        '''
        Сохранить структуры данных в XML файл.
        '''
        dump = Parser.writer( xmlfile, 'shop')
        dump.add_group('clients')
        dump.add_group('products')
        dump.add_group('sales')
        for client_key, client_val in self.__clients.items():
            dump.add_element('clients', 'client', client_val.as_dict())
        for product_key, product_val in self.__products.items():
            dump.add_element('products', 'product', product_val.as_dict())
        for sale_key, sale_val in self.__sales.items():
            dump.add_element('sales', 'sale', sale_val.as_dict())
        dump.dump()

    def save_to_sqlite(self, dbfile='db.sqlite3'):
        '''
        Сохранить результаты работы в базу данных SQLite3.
        '''
        print('Save to sqlite')

def main(argv):
    '''
    Здесь мы разбираем флаги командной строки и определяемся:
    - из файла или БД читать данные
    - в файл или в БД писать данные
    '''
    parser = argparse.ArgumentParser(description='Магазин')
    from_group = parser.add_mutually_exclusive_group()          #Создаем две взаимоисключающие группы
    to_group = parser.add_mutually_exclusive_group()            #куда записать и где прочитать
    from_group.add_argument('-x', '--xml',
        type=str,
        default='shop.xml',
        help='Прочитать начальные данные из XML файла')
    from_group.add_argument('-s', '--sqlite',
        type=str,
        help='Прочитать начальные данные из базы данных SQLite3')
    to_group.add_argument('-f', '--toxml',
        type=str,
        help='Сохранить данные в файл XML')
    to_group.add_argument('-d', '--tosqlite',
        type=str,
        help='Сохранить данные в базу данных SQLite3')
    args = parser.parse_args()
    application = runner()
    if args.xml:
        application.run_from_xml(args.xml, 'shop')
    if args.sqlite:
        application.run_from_sqlite(args.sqlite)
    if args.toxml:
        application.save_to_xml(args.toxml)
    if args.tosqlite:
        application.save_to_sqlite(args.tosqlite)


if __name__ == '__main__':
    main(sys)     #список аргументов командной строки

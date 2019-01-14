from collections import OrderedDict
import sqlite3


class db:
    __clients = {}
    __products = {}
    __sales = {}
    __client_attributes = []
    __product_attributes = []
    __sale_attributes = []
    __path = '' # Path to the database
    __conn = ''
    __cursor = ''

    __create_clients = 'CREATE TABLE {} ({})'
    __create_products = 'CREATE TABLE {} ({})'
    __create_sales = 'CREATE TABLE {} ({}) FOREIGN KEY clients.id, products.id'

    def __init__(self,
            path,
            clients,
            products,
            sales,
            client_attributes,
            product_attributes,
            sale_attributes):
        self.__clients = clients
        self.__client_attributes = client_attributes

        self.__products = products
        self.__product_attributes = product_attributes

        self.__sales = sales
        self.__sale_attributes = sale_attributes

        # Establish database connection
        self.__path = path
        self.__conn = sqlite3.connect(self.__path)
        self.__cursor = self.__conn.cursor()

    def __attr_list(self, alist):
        '''
        Склеить лист колоночек для создания таблички.
        '''
        attrs = ''
        for elem in alist:
            attrs = attrs + ', ' + elem

    def __create_table(self, tname, attrs, query):
        '''
        Создаём табличку. Принимаем её имя, список колоночек и шаблон
        SQL запроса.
        '''
        print('Creating table {}'.format(tname))
        print(query.format(tname, self.__attr_list(attrs)))
        self.__conn.execute(query.format(tname, self.__attr_list(attrs)))

    def save(self):
        '''
        Функция сохранения таблички.
        '''
        self.__create_table('clients', self.__client_attributes, self.__create_clients)
        self.__create_table('products', self.__product_attributes, self.__create_products)
        self.__create_table('sales', self.__sale_attributes, self.__create_sales)


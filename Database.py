from collections import OrderedDict
import sqlite3

import Client
import Product
import Sale

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

    __create_clients = '''
    CREATE TABLE IF NOT EXISTS {} ({});
    '''
    __create_products = '''
    CREATE TABLE IF NOT EXISTS {} ({});
    '''
    __create_sales = '''
    CREATE TABLE IF NOT EXISTS {}
    (
        {},
        FOREIGN KEY (client) REFERENCES clients(id),
        FOREIGN KEY (product) REFERENCES products(id)
    );
    '''

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
        self.__conn.row_factory = sqlite3.Row
        #self.__row_factory = self.__dict_factory
        #self.__row_factory = self.__dict_factory

    def __attr_list(self, alist, dots=False):
        '''
        Склеить лист колоночек для создания таблички.
        '''
        attrs = ''
        if not dots:
            for elem in alist:
                attrs += elem + ' TEXT' + ', '
        else:
            for elem in alist:
                attrs += ':' + elem + ', '
        attrs = attrs[:-2]
        return attrs

    def __create_table(self, tname, attrs, query):
        '''
        Создаём табличку. Принимаем её имя, список колоночек и шаблон
        SQL запроса.
        '''
        print('Creating table {}'.format(tname))
        print(query.format(tname, self.__attr_list(attrs)))
        self.__conn.execute(query.format(tname, self.__attr_list(attrs)))
        self.__conn.commit()

    def __dump_data(self, tname, attributes, objects):
        query = 'INSERT INTO {} VALUES ({})'.format(tname, self.__attr_list(attributes, True))
        print('Executing query: {}'.format(query))
        for key, value in objects.items():
            tmp_val = value.as_dict()
            tmp_val['id'] = key
            if 'product' in tmp_val:
                tmp_val['product'] = list(self.__products.keys())[list(self.__products.values()).index(value.getProduct())]
            if 'client' in tmp_val:
                tmp_val['client'] = list(self.__clients.keys())[list(self.__clients.values()).index(value.getClient())]
            self.__conn.execute(query, tmp_val)
        self.__conn.commit()

    def save(self):
        '''
        Функция сохранения таблички.
        '''
        self.__create_table('clients', self.__client_attributes, self.__create_clients)
        self.__create_table('products', self.__product_attributes, self.__create_products)
        self.__create_table('sales', self.__sale_attributes, self.__create_sales)

        self.__dump_data('clients', self.__client_attributes, self.__clients)
        self.__dump_data('products', self.__product_attributes, self.__products)
        self.__dump_data('sales', self.__sale_attributes, self.__sales)

    def __row2dict(self, inrow):
        return dict(zip(inrow.keys(), inrow))

    def __read_table(self, tname, objdict, objattribtes):
        self.__cursor = self.__conn.cursor()
        self.__cursor.execute('SELECT * FROM `{}`'.format(tname))
        rows = [dict(row) for row in self.__cursor]
        return rows

    def read(self):
        '''
        Почиталка из базы.
        '''
        clients = self.__read_table('clients', self.__clients, self.__client_attributes)
        products = self.__read_table('products', self.__products, self.__product_attributes)
        sales = self.__read_table('sales', self.__sales, self.__sale_attributes)

        for client in clients:
            client_obj = Client.client(client)                      #обходим конкретные атрибуты определенного клиента
            self.__clients[client['id']] = client_obj         #соотносим конкретному клиенту ID

        # Преобразуем dict клиентов в OrderedDict
        self.__clients = OrderedDict(sorted(self.__clients.items()))

        for product in products:
            product_obj = Product.product(product)
            self.__products[product['id']] = product_obj

        # Преобразуем dict продуктов в defaultdict
        self.__products = OrderedDict(sorted(self.__products.items()))

        for sale in sales:
            try:
                sale_obj = Sale.sale(sale, self.__products, self.__clients)
                self.__sales[sale['id']] = sale_obj
            except:
                if not sale['product'] in self.__products.keys():
                    print('Missing product reference: {}'.format(sale['product']))
                if not sale['client'] in self.__clients.keys():
                    print('Missing client reference: {}'.format(sale['client']))
        self.__sales = OrderedDict(sorted(self.__sales.items()))


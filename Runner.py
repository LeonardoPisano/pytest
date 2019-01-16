from collections import OrderedDict

import Client
import Product
import Sale
import Repl            # Читалка команд с терминала

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
    __sale_attributes = ('product',
        'client',
        'datsale',
        'datdelivery',
        'quantity',
        'id')
    __skip_attributes = ('id')
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
            try:
                client_obj = Client.client(client)                      #обходим конкретные атрибуты определенного клиента
                self.__clients[client['id']] = client_obj         #соотносим конкретному клиенту ID
            except:
                print('Unable to create client.')

        # Преобразуем dict клиентов в OrderedDict
        self.__clients = OrderedDict(sorted(self.__clients.items()))

        # Здесь мы получаем список словарей-продуктов
        # Каждый словарь это набор свойств одного продукта.
        products = shop_xml.get_entries(self.__product_attributes,
            'products',
            'product')
        # Мапим айдишники продуктов в объекты продуктов. Это нужно
        # для связи продаж с продуктами.
        for product in products:
            try:
                product_obj = Product.product(product)
                self.__products[product['id']] = product_obj
            except:
                print('Unable to create product.')

        # Преобразуем dict продуктов в defaultdict
        self.__products = OrderedDict(sorted(self.__products.items()))

        # Наконец, собираем список словарей продаж.
        sales = shop_xml.get_entries(self.__sale_attributes,
            'sales',
            'sale')

        #Конструируем объекты продаж, мапим их номера в объекты,
        #заодно подтягиваем айдишники клиентов.
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

        #for key, value in self.__sales:
         #   if value.getClient() in self.__perm.keys():
          #      self.__perm[value.getClient()] += value.getPrice() * value.getQuantity()
           # else:
            #    self.__perm[value.getClient()] = value.getPrice() * value.getQuantity()

    def run_from_sqlite(self, dbfile='shop.sqlite3'):
        '''
        Прочитать данные для работы из базы данных SQLite3.
        '''
        database = Database.db(dbfile,
            self.__clients,
            self.__products,
            self.__sales,
            self.__client_attributes,
            self.__product_attributes,
            self.__sale_attributes)
        database.read()

    def save_to_xml(self, xmlfile='new.xml'):
        '''
        Сохранить структуры данных в XML файл.
        '''
        dump = Parser.writer( xmlfile,'shop', self.__clients, self.__products)
        dump.add_group('clients')
        dump.add_group('products')
        dump.add_group('sales')
        for client_key, client_val in self.__clients.items():
            dump.add_element('clients', 'client', client_key, client_val)
        for product_key, product_val in self.__products.items():
            dump.add_element('products', 'product', product_key ,product_val)
        for sale_key, sale_val in self.__sales.items():
            dump.add_element('sales', 'sale', sale_key ,sale_val)
        dump.dump()

    def save_to_sqlite(self, dbfile='db.sqlite3'):
        '''
        Сохранить результаты работы в базу данных SQLite3.
        '''
        database = Database.db(dbfile,
            self.__clients,
            self.__products,
            self.__sales,
            self.__client_attributes,
            self.__product_attributes,
            self.__sale_attributes)
        database.save()


    def rep(self):
        '''
        Редактировать в консоли
        '''
        rep = Repl.repl(self.__clients,
            self.__products,
            self.__sales,
            self.__client_attributes,
            self.__product_attributes,
            self.__sale_attributes,
            self.__skip_attributes)
            #self.__perm)

        rep.reader()

from sys import stdin, stdout       #прием данных, вывод данных
import fileinput

import Client
import Product
import Sale

class repl:
    __client_attributes = []
    __product_attributes = []
    __sale_attributes = []
    # Имена атрибутов, которые не надо спрашивать и будут добавлены
    # автоматически.
    __skip_attributes = []

    __clients = dict()
    __products = dict()
    __sales = dict()
    #__perm = dict()

    __finput = fileinput.FileInput()

    def __init__(self,
        clients,
        products,
        sales,
        client_attributes,
        product_attributes,
        sale_attributes,
        skip_attributes):
        #perm):
        self.__clients = clients
        self.__products = products
        self.__sales = sales
        self.__client_attributes = client_attributes
        self.__product_attributes = product_attributes
        self.__sale_attributes = sale_attributes
        self.__skip_attributes = skip_attributes
        #self.__perm = perm

    def __print_elements(self, header, dict_val):
        print(header)
        for key, val in dict_val.items():
            print('{} {}'.format(key, val))

    def __print_obj(self, odict, dict_key):
        try:
            print('{} {}'.format(dict_key, odict[dict_key]))
        except:
            print('No such object.')

    def print(self):
        self.__print_elements('Клиенты:', self.__clients)
        self.__print_elements('Продукты:', self.__products)
        self.__print_elements('Продажи:', self.__sales)

    def __read_properties(self, properties):
        finput = fileinput.FileInput()
        obj = dict()
        for prop in properties:
            if not prop in self.__skip_attributes:
                obj[prop] = input('Введите значение для свойства: {}: '.format(prop))
        return obj

    def __add_element(self, eldict, obj):
        '''
        Добавить элемент с новым ключом в OrderedDict
        '''
        incremented_key = int(next(reversed(eldict))) + 1
        eldict[incremented_key] = obj

    def __remove_element(self, dict_val, del_index):
        del dict_val[del_index]

    def __check_client_used(self, client_index):
        client = self.__clients[client_index]
        for key, val in self.__sales.items():
            if client is val.getClient():
                return True
        return False

    def __check_product_used(self, product_index):
        product = self.__products[product_index]
        for key, val in self.__sales.items():
            if product is val.getProduct():
                return True
        return False

    def reader(self):
        line = ''
        while True:
            line = input('> ')
            if line.startswith('stop'):
                print('Stopping')
                break
            if line.startswith('print'):
                pargs = line.split()
                if len(pargs) == 3:
                    if pargs[1] == 'client':
                        self.__print_obj(self.__clients, pargs[2])
                    if pargs[1] == 'product':
                        self.__print_obj(self.__products, pargs[2])
                    if pargs[1] == 'sale':
                        self.__print_obj(self.__sales, pargs[2])
                else:
                    self.print()
                continue
            if line.startswith('new client'):
                properties = self.__read_properties(self.__client_attributes)
                client_obj = Client.client(properties)
                self.__add_element(self.__clients, client_obj)
                continue
            if line.startswith('new product'):
                print('Adding new product')
                properties = self.__read_properties(self.__product_attributes)
                product_obj = Product.product(properties)
                self.__add_element(self.__products, product_obj)
                continue
            if line.startswith('new sale'):
                print('Adding new sale')
                properties = self.__read_properties(self.__sale_attributes)
                sale_obj = Sale.sale(properties, self.__products, self.__clients)
                self.__add_element(self.__sales, sale_obj)
                continue
            if line.startswith('del client'):
                print('Deleting client')
                del_index = input('ID удаляемого объекта: ')
                if self.__check_client_used(del_index):
                    print('Клиент используется, невозможно удалить')
                else:
                    self.__remove_element(self.__clients, del_index)
                continue
            if line.startswith('del product'):
                print('Deleting product')
                del_index = input('ID удаляемого объекта: ')
                if self.__check_product_used(del_index):
                    print('Продукт используется, невозможно удалить')
                else:
                    self.__remove_element(self.__products, del_index)
                continue
            if line.startswith('del sale'):
                print('Deleting sale')
                del_index = input('ID удаляемого объекта: ')
                self.__remove_element(self.__sales, del_index)
                continue
            print('Неопознанная команда: {}'.format(line))


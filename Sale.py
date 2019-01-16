import datetime

class sale:                #класс продаж
    def __init__(self, propdict, productdict, clientdict):
        self.__product = productdict[propdict['product']]
        self.__client = clientdict[propdict['client']]
        datetime.datetime.strptime(propdict['datsale'], '%d.%m.%Y')
        self.__datsale = propdict['datsale']
        datetime.datetime.strptime(propdict['datdelivery'], '%d.%m.%Y')
        self.__datdelivery = propdict['datdelivery']
        self.__quantity = propdict['quantity']

    def __str__(self):
        return '{}{} {} '.format(self.__product,
                                       self.__quantity,
                                       self.__client)

    def setProduct(self,value):                        #Устанавливает значение атрибутов
        self.__product=value

    def setClient(self,value):
        self.__client=value

    def setDatsale(self,value):
        self.__datsale = valuе

    def setDatdelivery(self,value):
        self.__datdelivery=value

    def setQuantity(self,value):
        self.__quantity=value

    def getProduct(self):                                #Возвращает значение атрибутов
        return self.__product

    def getClient(self):
        return self.__client

    def getDatsale(self):
        return self.__datsale

    def getDatdelivery(self):
        return self.__datdelivery

    def getQuantity(self):
        return self.__quantity

    def as_dict(self):
        '''
        Вернуть все свойства продукта в виде словаря
        '''
        return { 'product': self.__product,
            'client': self.__client,
            'datsale': self.__datsale,
            'datdelivery': self.__datdelivery,
            'quantity': self.__quantity }

class sale:                #класс продаж
    def __init__(self, propdict, productdict, clientdict):
        self.__product = productdict[propdict['product']]
        self.__client = clientdict[propdict['client']]
        self.__datsale = propdict['datsale']
        self.__datdelivery = propdict['datdelivery']

    def __str__(self):
        return '\"{}\" \"{}\"'.format(self.__product,
            self.__client)

    def setProduct(self,value):                        #Устанавливает значение атрибутов
        '''
        Установить ссылку на объек типа product с идентификатором ID
        '''
        self.__product=value

    def setClient(self,value):
        '''
        Установить ID покупателя.
        '''
        self.__client=value

    def setDatsale(self,value):
        '''
        Установить дату продажи.
        '''
        self.__datsale=value

    def setDatdelivery(self,value):
        '''
        Установить дату доставки.
        '''
        self.__datdelivery=value

    def getProduct(self):                                #Возвращает значение атрибутов
        '''
        Возвращаем название продукта.
        '''
        return self.__product

    def getClient(self):
        '''
        Возвращаем имя клиента.
        '''
        return self.__client

    def getDatsale(self):
        '''
        Возвращаем значение дату продажи.
        '''
        return self.__datsale

    def getDatdelivery(self):
        '''
        Возвращаем дату  доставки.
        '''
        return self.__datdelivery

    def as_dict(self):
        '''
        Вернуть все свойства продукта в виде словаря
        '''
        return { 'product': self.__product,
            'client': self.__client,
            'datsale': self.__datsale,
            'datdelivery': self.__datdelivery }


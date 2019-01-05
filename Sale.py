class sale:                #класс продаж
    def __init__(self, propdict, productdict, clientdict):
        self.setProduct(productdict[propdict['product']])
        self.setClient(clientdict[propdict['client']])
        self.setDatsale(propdict['datsale'])
        self.setDatdelivery(propdict['datdelivery'])
        self.setNumber(propdict['number'])

    def __str__(self):
        return 'product {} client {} datsale {} datdelivery {} number {}'.format(self.getProduct().getDesignation(),         #сериализация
                                                                                 self.getClient().getName(),
                                                                                 self.getDatsale(),
                                                                                 self.getDatdelivery(),
                                                                                 self.getNumber())

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

    def setNumber(self,value):
        '''
        Установить количество покупаемого продукта.
        '''
        self.__number=value


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

    def getNumber(self):
        '''
        Возвращаем количество заказанных продуктов.
        '''
        return self.__number

    def as_dict(self):
        '''
        Вернуть все свойства продукта в виде словаря
        '''
        return { 'product': self.__product,
            'client': self.__client,
            'datsale': self.__datsale,
            'datdelivery': self.__datdelivery,
            'number': self.__number }


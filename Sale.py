class sale:                #класс продаж
    def __init__(self, product='', client='', datsale='', datdelivery='', number=''):      # Описание конструктора класса
        self.setProduct(product)
        self.setClient(client)                                 
        self.setDatsale(datsale)               
        self.setDatdelivery(datdelivery)
        self.setNumber(number)
        
    def setProduct(self,value):                          #Устанавливает значение атрибутов
        '''
        Установить ID проданного продукта.
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


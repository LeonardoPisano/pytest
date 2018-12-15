class product:                #класс товаров
    def __init__(self, propdict):
        self.setDesignation(propdict['designation'])
        self.setPrice(propdict['price'])
        self.setUnit(propdict['unit'])
        self.setID(propdict['id'])

    def setDesignation(self,value):         #Устанавливает значение атрибутов
        '''
        Устанавливаем название продукта.
        '''
        self.__designation=value

    def setPrice(self,value):
        '''
        Устанавливаем цену продукта.
        '''
        self.__price=value

    def setUnit(self,value):
        '''
        Устанавливем единицу измерения данного продукта.
        '''
        self.__unit=value

    def setID(self, pid):
        '''
        Устанавливаем ID продукта
        '''
        self.__pid = pid

    def getDesignation(self):                  #Возвращает значение атрибутов
        '''
        Возвращаем название продукта.
        '''
        return self.__designation

    def getPrice (self):
        '''
        Возвращаем значение цены.
        '''
        return self.__price

    def getUnit (self):
        '''
        Возвращаем единицы измерения.
        '''
        return self.__unit

    def getID(self):
        '''
        Возвращаем ID продукта
        '''
        return self.__pid

    def as_dict(self):
        '''
        Вернуть все свойства объекта в виде словаря.
        '''
        return { 'designation': self.__designation,
            'price': self.__price,
            'unit': self.__unit,
            'id': self.__pid }

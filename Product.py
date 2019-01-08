class product:                #класс товаров
    def __init__(self, propdict):
        self.__designation = propdict['designation']
        self.__price = propdict['price']
        self.__unit = propdict['unit']

    def __str__(self):
        return '\"{}\" {} {} руб.'.format(self.__designation,
            self.__unit,
            self.__price)

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

    def as_dict(self):
        '''
        Вернуть все свойства объекта в виде словаря.
        '''
        return { 'designation': self.__designation,
            'price': self.__price,
            'unit': self.__unit }


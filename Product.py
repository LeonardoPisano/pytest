class product:                #класс товаров
    def __init__(self, propdict):
        self.__designation = propdict['designation']
        self.__price = propdict['price']
        self.__unit = propdict['unit']
        #self.__saledict = saledict[propdict['sale']]

    def __str__(self):
        return '\'{}\' {} руб. {}. '.format(self.__designation,
            #self.__quantity,                #количество купленных продуктов
            self.__price,
            self.__unit)

    #def setSale(self,value):
     #   self.__sale=value

    def setDesignation(self,value):         #Устанавливает значение атрибутов
        self.__designation=value

    def setPrice(self,value):
        self.__price=value

    def setUnit(self,value):
        self.__unit=value

    #def getSale(self):
     #   return salf.__sale

    def getDesignation(self):                  #Возвращает значение атрибутов
        return self.__designation

    def getPrice (self):
        return self.__price

    def getUnit (self):
        return self.__unit

    def as_dict(self):
        return { 'designation': self.__designation,
            'price': self.__price,
            'unit': self.__unit }


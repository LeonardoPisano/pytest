class product:                #класс товаров
    def __init__(self,designation='', price=0, unit=''):      # Описание конструктора класса
        self.setDesignation(designation)                      
        self.setPrice(price)                                 
        self.setUnit(unit)             
        
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




        

class product:                #класс товаров
    def __init__(self,designation='', price=0, unit=''):      # Описание конструктора класса
        self.setDesignation(designation)                      
        self.setPrice(price)                                 
        self.setUnit(unit)             
        
    def setDesignation(self,value):self.__designation=value     #Устанавливает значение атрибутов
    def setPrice(self,value):self.__price=value                   
    def setUnit(self,value):self.__unit=value
    
    def getDesignation(self):return self.__designation          #Возвращает значение атрибутов
    def getPrice (self):return self.__price
    def getUnit (self):return self.__unit




        

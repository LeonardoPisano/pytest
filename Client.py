class client:                #класс клиентов
    def __init__(self, surname='', name='', secname='', address='', phone='', email='', permanent=''):      # Описание конструктора класса
        self.setSurname(surname)                      
        self.setName(name)                                 
        self.setSecname(secname)  
        self.setAddress(address)
        self.setPhone(phone)
        self.setEmail(email)
        self.setPermanent(permanent)
        
    def setSurname (self,value):self.__surname=value     #Устанавливает значение атрибутов
    def setName (self,value):self.__name=value                   
    def setSecname (self,value):self.__secname=value
    def setAddress (self, value):self.__address=value
    def setPhone (self, value):self.__phone=value
    def setEmail (self, value):self.__email=value
    def setPermanent (self, value):self.__permanent=value
    
    
    def getSurname (self):return self.__surname         #Возвращает значение атрибутов
    def getName (self):return self.__name
    def getSecname (self):return self.__secname
    def getAddress (self):return self.__address
    def getPhone (self):return self.__phone
    def getEmail (self):return self.__email
    def getPermanent (self):return self.__permanent


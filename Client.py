class client:                #класс клиентов
    def __init__(self,
            surname='',
            name='',
            secname='',
            address='',
            phone='',
            email='',
            permanent=''):      # Описание конструктора класса
        self.setSurname(surname)                      
        self.setName(name)                                 
        self.setSecname(secname)  
        self.setAddress(address)
        self.setPhone(phone)
        self.setEmail(email)
        self.setPermanent(permanent)

    def setSurname (self,value):                 #Устанавливает значение атрибутов
        '''
        Устанавливаем фамилию клиента.
        '''
        self.__surname=value

    def setName (self,value):
        '''
        Устанавливаем имя клиента.
        '''
        self.__name=value

    def setSecname (self,value):
        '''
        Устанавливаем отчество клиента.
        '''
        self.__secname=value

    def setAddress (self, value):
        '''
        Устанавливаем адрес клиента.
        '''
        self.__address=value

    def setPhone (self, value):
        '''
        Устанавливаем телефон клиента.
        '''
        self.__phone=value

    def setEmail (self, value):
        '''
        Устанавливаем Email клиента.
        '''
        self.__email=value

    def setPermanent (self, value):
        '''
        Устанавливаем критерий постоянного\не постояннного клиента.
        '''
        self.__permanent=value

    def getSurname (self):                  #Возвращает значение атрибутов
        '''
        Возвращаем значение фамилии.
        '''
        return self.__surname  

    def getName (self):
        '''
        Возвращаем значение имя.
        '''
        return self.__name

    def getSecname (self):
        '''
        Возвращаем значение отчества.
        '''
        return self.__secname

    def getAddress (self):
        '''
        Возвращаем значение адреса.
        '''
        return self.__address

    def getPhone (self):
        '''
        Возвращаем значение телефона.
        '''
        return self.__phone

    def getEmail (self):
        '''
        Возвращаем значение Email.
        '''
        return self.__email

    def getPermanent (self):
        '''
        Возвращаем значение постоянного\не постояннного клиента.
        '''
        return self.__permanent


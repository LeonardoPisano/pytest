class client:                #класс клиентов
    def __init__(self, propdict):
        self.setName(propdict['name'])
        self.setSurname(propdict['surname'])
        self.setSecname(propdict['secname'])
        self.setAddress(propdict['address'])
        self.setPhone(propdict['phone'])
        self.setEmail(propdict['email'])
        self.setPermanent(propdict['permanent'])
        self.setID(propdict['id'])

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

    def setID(self, cid):
        '''
        Установить ID клиента
        '''
        self.__id = cid

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

    def getID(self):
        '''
        Вернуть ID клиента
        '''
        return self.__id

    def as_dict(self):
        '''
        Вернуть все свойства объекта в виде словаря.
        '''
        return { 'name': self.__name,
            'surname': self.__surname,
            'secname': self.__secname,
            'address': self.__address,
            'phone': self.__phone,
            'email': self.__email,
            'permanent': self.__permanent,
            'id': self.__id }


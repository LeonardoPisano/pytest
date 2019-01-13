import re

class client:                #класс клиентов
    __re_email = re.compile(r'[^@]+@[^@]+\.[^@]+')
    def __init__(self, propdict):
        self.setName(propdict['name'])
        self.setSurname(propdict['surname'])
        self.setSecname(propdict['secname'])
        self.setAddress(propdict['address'])
        self.setPhone(propdict['phone'])
        self.setEmail(propdict['email'])
        self.setPermanent(propdict['permanent'])

    def __str__(self):
        return '\"{} {} {}\"'.format(self.__surname,
            self.__name,
            self.__secname)

    def setSurname (self,value):                 #Устанавливает значение атрибутов (экземпляры)
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

    def setEmail (self, value):             #описать структуру email регулярных выражений 
        '''
        Устанавливаем Email клиента.
        '''
        if self.__re_email.match(value):
            self.__email=value
        else:
            raise Exception('invalid email {}'.format(value))

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
            'permanent': self.__permanent }


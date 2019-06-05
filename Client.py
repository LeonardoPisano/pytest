import re
import Product

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
        self.__surname=value

    def setName (self,value):
        self.__name=value

    def setSecname (self,value):
        self.__secname=value

    def setAddress (self, value):
        self.__address=value

    def setPhone (self, value):
        self.__phone=value

    def setEmail (self, value):             #описать структуру email регулярных выражений 
        if self.__re_email.match(value):
            self.__email=value
        else:
            raise Exception('invalid email {}'.format(value))

    def setPermanent (self, value):
        #if self.__priduct.prise(value) * self.__sale.quantity(value) > 5000:       #или нужно сделать ссылки и создать новые переменные???
         #   self.__permanent=1
        #else:
        self.__permanent=value
    def getSurname (self):                  #Возвращает значение атрибутов
        return self.__surname

    def getName (self):
        return self.__name

    def getSecname (self):
        return self.__secname

    def getAddress (self):
        return self.__address

    def getPhone (self):
        return self.__phone

    def getEmail (self):
        return self.__email

    def getPermanent (self):
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

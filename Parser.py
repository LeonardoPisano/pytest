import xml.dom.minidom as md   #Стандартная поставка в python

import Client           #импортируем модули
import Product
import Sale

class writer:
    __xmldoc = md.Document()
    __dumpname = ''     #имя файла shop.xml в который сохранять данные
    __rootname = ''     #имя корнегого элемента <shop> </shop>
    __rootnode = ''     #корневая нода
    __clients = dict()
    __products = dict()

    def __init__(self, dumpname,
                 rootnode,
                 clients,
                 products):
        '''
        Создаёт объект XML документа, который должен быть записан
        в файл.
        '''
        self.__dumpname = dumpname
        self.__rootname = rootnode
        root = self.__xmldoc.createElement(self.__rootname)                                 #создать элемент
        self.__xmldoc.appendChild(root)                                                     #возвращаем ссылку и дабавляет элемент
        self.__rootnode = self.__xmldoc.getElementsByTagName(self.__rootname)[0]            #собираем нужные части из XML
        self.__clients = clients
        self.__products = products

    def add_group(self, groupname):
        '''
        Добавляет группу в корневой элемент.
        '''
        xmlgroup = self.__xmldoc.createElement(groupname)
        self.__rootnode.appendChild(xmlgroup)

    def add_element(self, groupname, elemname, el_key, el_val):
        '''
        Вставляет элемент elemname с атрибутами из словаря attributes в
        группу groupname.
        '''
        subgroup = self.__rootnode.getElementsByTagName(groupname)[0]
        newelem = self.__xmldoc.createElement(elemname)
        for attr, value in el_val.as_dict().items():
            if attr == 'client':
                newelem.setAttribute(attr, list(self.__clients.keys())[list(self.__clients.values()).index(el_val.getClient())])
                continue

            if attr == 'product':
                newelem.setAttribute(attr, list(self.__products.keys())[list(self.__products.values()).index(el_val.getProduct())])
                continue

            newelem.setAttribute(attr, value)
        subgroup.appendChild(newelem)

    def dump(self):
        '''
        Сбросить сконструированный объект XML в файл __dumpname.
        '''
        handle = open(self.__dumpname, 'w')
        self.__xmldoc.writexml(writer=handle,
            indent='',
            addindent='\t',
            newl='\n')
        handle.close()


class parser:

    __filename = ''     #имя файла
    __rootnode = ''
    def __init__(self, docname, rootnode):
        #print('Разбираем файл XML: {}'.format(docname))
        # Читаем XML файл с начальными данными в DOM дерево
        domtree = md.parse(docname) #parse - разбираем файл
        domtree.normalize() 

        # Берём корневой элемент документа
        self.__filename = docname
        self.__rootnode = domtree.getElementsByTagName(rootnode)[0] #Обращаемся к первому элементу с этим именем

    def parse_group_for(self, groupname, elemname):
        '''
        Выбрать элементы elemname из группы groupname
        '''
        #print('Выбираем элементы {} из группы {}\n'.format(elemname, groupname))
        #print('\n')
        return self.__rootnode.getElementsByTagName(groupname)[0].getElementsByTagName(elemname)

    def get_attributes(self, entry, attributes):
        '''
        Выбрать все атрибуты из одного элемента XML и вернуть их в
        виде словаря.
        '''
        element = dict()
        for attr in attributes:
            if entry.hasAttribute(attr):                        #если такой элемент существует, то
                element[attr] = entry.getAttribute(attr)        #создать ключ этого элемента для словаря
            else:
                raise  Exception('No attribute named {} found in entry.'.format(attr))

        return element

    def get_entries(self, attrlist, groupname, elemname):
        '''
        Выбрать все элементы атрибуты attrlist из элементов elemname
        из группы groupname и вернуть в виде списка словарей.
        '''
        #print('\nСоздаём список элементов {} из группы {}'.format(elemname, groupname))
        entries = self.parse_group_for(groupname, elemname)
        entry_list = []
        for entry in entries:           #обходим список элементов, собираем их атрибуты
            try:
                entry_list.append(self.get_attributes(entry, attrlist))
            except Exception as error:
                print ('Caught exception while geting attributes: {}'.format(repr (error)))
        return entry_list #возвращаем список словарей


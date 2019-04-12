#!/usr/bin/env python3.6
import xml.dom.minidom as md
import argparse     #модуль для обработки аргументов командной строки
import sys          #предоставляет системе особые параметры и функции

import Runner

def main(argv):
    '''
    Здесь мы разбираем флаги командной строки и определяемся:
    - из файла или БД читать данные
    - в файл или в БД писать данные
    '''
    parser = argparse.ArgumentParser(description='Магазин')
    from_group = parser.add_mutually_exclusive_group()          #Создаем две взаимоисключающие группы
    to_group = parser.add_mutually_exclusive_group()            #куда записать и где прочитать
    from_group.add_argument('-x', '--xml',
        type=str,
        default='shop.xml',
        help='Прочитать начальные данные из XML файла')
    from_group.add_argument('-s', '--sqlite',
        type=str,
        help='Прочитать начальные данные из базы данных SQLite3')
    to_group.add_argument('-f', '--toxml',
        type=str,
        help='Сохранить данные в файл XML')
    to_group.add_argument('-d', '--tosqlite',
        type=str,
        help='Сохранить данные в базу данных SQLite3')
    args = parser.parse_args()
    application = Runner.runner()
    if args.sqlite:
        print('Starting from SQLite3 database.')
        application.run_from_sqlite(args.sqlite)
    else:
        print('Starting from XML file.')
        application.run_from_xml(args.xml, 'shop')

    #application.rep()
    application.gui()

    if args.toxml:
        print('Saving to XML file.')
        application.save_to_xml(args.toxml)
    if args.tosqlite:
        print('Saving to SQLite3 database.')
        application.save_to_sqlite(args.tosqlite)

if __name__ == '__main__':
    main(sys)     #список аргументов командной строки

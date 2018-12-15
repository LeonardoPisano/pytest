#!/usr/local/bin/python3.6
import xml.dom.minidom as md

import Client
import Product
import Sale

def main():
    # Читаем XML файл с начальными данными в DOM дерево
    domtree = md.parse("shop.xml")
    domtree.normalize()

    # Забираем группы clients, products и sales из XML
    clients = domtree.getElementsByTagName("clients")[0].childNodes
    products = domtree.getElementsByTagName("products")[0].childNodes
    sales = domtree.getElementsByTagName("sales")[0].childNodes

    # Собрать список клиентов
    for client in clients
        

    # Собрать список продуктов

    # Собрать список продаж

if __name__ == '__main__':
    main()


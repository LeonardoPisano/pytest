#!/usr/bin/env python2

class qwe:
    value_text = 'Value: '

    def __init__(self, value):
        self.initial_value = value**2

    def print_value(self):
        print('{}{}'.format(self.value_text, self.initial_value))

if __name__ == '__main__':
    class_instance = qwe(22) 
    class_instance.print_value()


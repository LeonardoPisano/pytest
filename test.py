#!/usr/bin/env python2

class AppRunner:
    testvar = 123
    
    def run(self):
        print ('hello, world: {}'.format(self.testvar))

if __name__ == '__main__':
    test = AppRunner()
    test.testvar = 'test1'
    test.run()
    
    test2 = AppRunner()
    test2.testvar = 'test2'
    test2.run()

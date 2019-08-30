'''
Created on Aug 29, 2019

@author: travi
'''
from pad import left

class AppMain:
    '''
    Additional test class put in place while working on the gherkin/behave test suite.
    '''
    def __init__(self):
        print('initializing AppMain')
        
    def test_left_padded_input(self):        
        print('100 as a left-padded fixed-length string: ' + left('100', '0', 10))
        
if __name__ == '__main__':
    appMain = AppMain()
    appMain.test_left_padded_input()

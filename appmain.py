'''
Created on Aug 29, 2019

@author: travis steinmetz
'''
import logging
from pad import Pad


layout = '%(asctime)-10s | ' \
         '%(levelname)-8s | ' \
         '%(lineno)4s | ' \
         '%(filename)24s | ' \
         '%(processName)24s | ' \
         '%(funcName)24s | ' \
         '%(message)s'

logging.basicConfig(
    # filename='pad.log',
    level=logging.DEBUG,
    format=layout,
    datefmt='%Y-%m-%d %H:%M:%S'
)

log = logging.getLogger(__name__)


class AppMain:

    """
    Additional test class put in place while working on the gherkin/behave test suite.
    """
    def __init__(self):
        log.debug('initializing AppMain')

    def test_left_padded_input(self):        
        log.debug('100 as a left-padded fixed-length string: %s', Pad.left('100', '0', 10))
        log.debug('Courtesy amount ($1,021.65) as a left-padded fixed-length string: %s', Pad.left('$1,021.65', ' ', 16))

    def test_right_padded_input(self):

        log.debug('Legal amount ($1,021.65) as a right-padded fixed-length string: %s',
                  Pad.right('One thousand twenty-one dollars and 65 cents', '*', 64))
        
if __name__ == '__main__':
    appMain = AppMain()
    appMain.test_left_padded_input()
    appMain.test_right_padded_input()

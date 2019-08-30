'''
Created on Aug 21, 2019

@author: travis l. steinmetz

References:

[1] https://wiki.python.org/moin/HandlingExceptions
[2] https://docs.python-guide.org/writing/structure/
[3] https://stackoverflow.com/questions/3289601/null-object-in-python
'''

import sys
from builtins import int, isinstance

def is_valid_input(source_string, padding_character, output_length):
    '''
    Method used to provide basic validation on input parameters. It checks for None aka null values,
    ensures the proper type is presented, determines if the input is an empty string, and does basic
    data validation such as length checking. It is used by both .left() and .right() padding operations.
    '''
    valid_input = True
    
    if not source_string or not isinstance(source_string, str) or source_string == '':
        print('source_string cannot be None or empty')
        valid_input = False
    
    if not padding_character or not isinstance(padding_character, str) or padding_character == '':
        print('padding_character cannot be None or empty')
        valid_input = False
        
    if not isinstance(output_length, int) or output_length <  len(source_string):
        print(
            'output_length cannot be less than the length of source_string ' +
            'output_length: ' + str(output_length) + ' ' +
            'source_string: ' + str(source_string)
             )
        valid_input = False
        
    return valid_input

def left(source_string, padding_character, output_length):
    '''
    source_string - the string to pad
    padding_character - the character to pad the given source_string with
    output_length - the overall length of the padded string
    '''
    left_padded_string = ''
    
    try:
        if is_valid_input(source_string, padding_character, output_length):
            print(
                'input parameters -> source_string: ' + source_string + ' | ' + 
                'padding_character: ' + padding_character + ' | ' +
                'output_length: ' + str(output_length) 
                )
        
            left_padded_string = padding_character[0]*(output_length - len(source_string)) + source_string
        else:
            print('Invalid input received, aborting padding operation.')
            
        return left_padded_string 
            
    except:
        print('Unexpected error: ', sys.exc_info()[0])

def right(source_string, padding_character, output_length):
    '''
    source_string - the string to pad
    padding_character - the character to pad the given source_string with
    output_length - the overall length of the padded string
    '''
    right_padded_string = ''
    
    try:
        if is_valid_input(source_string, padding_character, output_length):
            print(
                'input parameters -> source_string: ' + source_string + ' | ' + 
                'padding_character: ' + padding_character + ' | ' +
                'output_length: ' + str(output_length)
                )
        
            right_padded_string = source_string + padding_character[0]*(output_length - len(source_string))
        else:
            print('Invalid input received, aborting padding operation.')
            
        return right_padded_string
    
    except:
        print('Unexpected error: ', sys.exc_info()[0])
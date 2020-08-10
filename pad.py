'''
Created on Aug 21, 2019

@author: travis l. steinmetz

References:

[1] https://wiki.python.org/moin/HandlingExceptions
[2] https://docs.python-guide.org/writing/structure/
[3] https://stackoverflow.com/questions/3289601/null-object-in-python
[4] https://realpython.com/python-logging/#basic-configurations
'''

import logging
from builtins import int, isinstance

log = logging.getLogger(f'__main__{__name__}')


class Pad:
    def __init__(self):
        log.info(f'initializing {self.__class__.__name__}')

    @staticmethod
    def is_none_or_empty(target):
        """
        Provides basic string validation, verifying that the input is a string data type, is a valid object, and is not
        emtpy.
        :return: True if the input is not None and is a non-empty string; otherwise, returns False
        """
        valid_input = False
        try:
            if target:
                if isinstance(target, str):
                    if target == '':
                        log.warning('target: >%s< Issue: is empty.', target)
                    else:
                        valid_input = True
                else:
                    log.warning('target: %s Issue: is not a str', target)
            else:
                log.warning('target: %s Issue: is None', target)
        except Exception as e:
            log.warning('Unexpected error encountered. Input is assumed invalid. Error: %s', e)

        return valid_input

    @staticmethod
    def is_valid_input(source_string, padding_character, output_length):
        '''
        Method used to provide basic validation on input parameters. It checks for None aka null values,
        ensures the proper type is presented, determines if the input is an empty string, and does basic
        data validation such as length checking. It is used by both .left() and .right() padding operations.
        '''
        valid_input = True

        if not Pad.is_none_or_empty(source_string):
            log.warning('source_string cannot be None or empty')
            valid_input = False

        if not Pad.is_none_or_empty(padding_character):
            log.warning('padding_character cannot be None or empty')
            valid_input = False

        if not isinstance(output_length, int) or output_length < len(source_string):
            log.warning('output_length cannot be less than the length of source_string - output_length: %s source_string: %s', output_length, source_string)
            valid_input = False

        return valid_input

    @staticmethod
    def left(source_string, padding_character, output_length):
        '''
        source_string - the string to pad
        padding_character - the character to pad the given source_string with
        output_length - the overall length of the padded string
        '''
        left_padded_string = ''

        try:
            if Pad.is_valid_input(source_string, padding_character, output_length):
                log.debug('source_string: %s padding_character: %s output_length: %s', source_string,
                                                                                       padding_character,
                                                                                       output_length)
                left_padded_string = padding_character[0]*(output_length - len(source_string)) + source_string
                log.debug('left_padded_string: %s', left_padded_string)
            else:
                log.warning('Invalid input received, aborting padding operation.')

            return left_padded_string

        except Exception as e:
            log.warning('WARNING: %s', e)

    @staticmethod
    def right(source_string, padding_character, output_length):
        '''
        source_string - the string to pad
        padding_character - the character to pad the given source_string with
        output_length - the overall length of the padded string
        '''
        right_padded_string = ''

        try:
            if Pad.is_valid_input(source_string, padding_character, output_length):
                log.debug('source_string: %s padding_character: %s output_length: %s', source_string,
                                                                                       padding_character,
                                                                                       output_length)
                right_padded_string = source_string + padding_character[0]*(output_length - len(source_string))
                log.debug('right_padded_string: %s', right_padded_string)
            else:
                log.warning('Invalid input received, aborting padding operation.')

            return right_padded_string

        except Exception as e:
            log.warning('WARNING: %s', e)


from behave import given, when, then
from pad import Pad

@given(u'a source string of value 100')
def initialize_source_string(context):
    context.source_string = '100'

@given(u'a padding character of 0')
def initialize_padding_character(context):
    context.padding_character = '0'

@given(u'an overall length of 10')
def initialize_overall_length(context):
    context.output_length = 10

@when(u'I invoke the left method with valid parameters')
def create_fixed_length_left_padded_string(context):
    assert(context.source_string is None) is False
    assert(context.padding_character is None) is False
    assert(context.output_length is None or context.output_length == 0) is False
    
    context.left_padded_output = Pad.left(context.source_string, context.padding_character, context.output_length)
    print("left_padded_output: " + context.left_padded_output)
    assert(context.left_padded_output is None) is False

@then(u'I expect to receive a string with value 0000000100 in the response')
def verify_string(context):
    assert('0000000100' == context.left_padded_output) is True

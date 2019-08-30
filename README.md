# Pad
Python utility project demonstrating how to create a fixed-length string that is padded (left/right) with a given padding character, i.e. **left('100', '0', 10) ==> '0000000100'**. Also demonstrates how to integrate *Behave (BDD) testing*.

## Project Structure

./features - Source folder for *.feature* files that are written using **Gherkin**.

./features/steps - Source folder for **.py* files using the **Behave** features such as *given, when, then,* etc.

## Expected Test Output
```
C:\Users\travi\eclipse-workspace\Pad>behave
@left_padded_string_positive_case
Feature: Create a fixed-length string that is left padded. # features/pad_left.feature:21

  @left_padded_fixed_length_string
  Scenario: Left padded fixed length string                                 # features/pad_left.feature:23
    Given a source string of value 100                                      # features/steps/left_pad_a_string_test.py:5
    And a padding character of 0                                            # features/steps/left_pad_a_string_test.py:9
    And an overall length of 10                                             # features/steps/left_pad_a_string_test.py:13
    When I invoke the left method with valid parameters                     # features/steps/left_pad_a_string_test.py:17
    Then I expect to receive a string with value 0000000100 in the response # features/steps/left_pad_a_string_test.py:27

1 feature passed, 0 failed, 0 skipped
1 scenario passed, 0 failed, 0 skipped
5 steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m0.001s
```

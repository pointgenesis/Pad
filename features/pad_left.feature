#Author: travis.steinmetz@gmail.com
#Keywords Summary : Test cases for fixed-length strings that are left padded.
#Feature: List of scenarios.
#Scenario: Business rule through list of steps with arguments.
#Given: Some precondition step
#When: Some key actions
#Then: To observe outcomes or validation
#And,But: To enumerate more Given,When,Then steps
#Scenario Outline: List of steps for data-driven as an Examples and <placeholder>
#Examples: Container for s table
#Background: List of steps run before each of the scenarios
#""" (Doc Strings)
#| (Data Tables)
#@ (Tags/Labels):To group Scenarios
#<> (placeholder)
#""
## (Comments)
#Sample Feature Definition Template

@left_padded_string_positive_case
Feature: Create a fixed-length string that is left padded.
  @left_padded_fixed_length_string
  Scenario: Left padded fixed length string
    Given a source string of value 100
    And a padding character of 0
    And an overall length of 10
    When I invoke the left method with valid parameters
    Then I expect to receive a string with value 0000000100 in the response
    
#
    #When I complete action
    #And some other action
    #And yet another action
    #Then I validate the outcomes
    #And check more outcomes
#
  #@tag2
  #Scenario Outline: Title of your scenario outline
    #Given I want to write a step with <name>
    #When I check for the <value> in step
    #Then I verify the <status> in step
#
    #Examples: 
      #| name  | value | status  |
      #| name1 |     5 | success |
      #| name2 |     7 | Fail    |

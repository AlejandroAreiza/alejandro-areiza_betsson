Feature: Smoke Test - Environment Setup Verification
  As a tester
  I want to verify the test environment is set up correctly
  So that I can ensure all components are working

  Scenario Outline: Verify current activity is correct
    Given the SwapLabsApp
    When I get the current activity
    Then the activity name should be "<activity_name>"

    Examples:
    | activity_name     |
    | .MainActivity     |
    | .ProductActivity  |

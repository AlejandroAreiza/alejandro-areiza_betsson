Feature: Smoke Test - Application Launch Verification
  As a tester
  I want to verify the application launches correctly
  So that I can ensure the test environment is ready for testing

  Scenario: Verify login screen is displayed on app launch
    Given the Swag Labs app is installed and launched
    Then I am on the login screen
    And the login button should be visible

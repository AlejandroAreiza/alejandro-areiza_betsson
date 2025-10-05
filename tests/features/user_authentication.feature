Feature: User Authentication
  As a user
  I want secure login validation
  So that only authorized users can access the app

  Background:
    Given the Swag Labs app is installed and launched
    And I am on the login screen

  # Scenario Outline: Successful login with valid user credentials
  #   When I login with username "<user_name>" and password "<user_password>"
  #   Then I should be navigated to the "Products" screen
  #   And I should see the products catalog
  #   And the screen title should display "PRODUCTS"
  #   And the cart icon should be visible in the navigation bar

  #   Examples:
  #     | user_name     | user_password |
  #     | standard_user | secret_sauce  |
  #     | problem_user  | secret_sauce  |

  Scenario Outline: Login attempt with invalid credentials
    When I login with username "<user_name>" and password "<user_password>"
    Then I should see an error message
    And the error message should contain "<error_text>"

    Examples:
      | user_name       | user_password | error_text                                                      |
      | invalid_user    | secret_sauce  | Username and password do not match any user in this service     |
      | standard_user   | wrong_pass    | Username and password do not match any user in this service     |
      | STANDARD_USER   | secret_sauce  | Username and password do not match any user in this service     |
      |    <empty>      | secret_sauce  | Username is required                                            |
      | standard_user   |    <empty>    | Password is required                                            |
      |    <empty>      |    <empty>    | Username is required                                            |
      | locked_out_user | secret_sauce  | Sorry, this user has been locked out                            |

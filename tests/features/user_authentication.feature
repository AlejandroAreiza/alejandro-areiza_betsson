Feature: User Authentication
  As a registered user
  I want to log into the Swag Labs app
  So that I can access the product catalog and make purchases

  Background:
    Given the Swag Labs app is installed and launched
    And I am on the login screen

  Scenario Outline: Successful login with valid user credentials
    When I login with username "<user_name>" and password "<user_password>"
    Then I should be navigated to the "Products" screen
    And I should see the products catalog
    And the screen title should display "PRODUCTS"
    And the cart icon should be visible in the navigation bar

    Examples:
      | user_name     | user_password |
      | standard_user | secret_sauce  |
      | problem_user  | secret_sauce  |

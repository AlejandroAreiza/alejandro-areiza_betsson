Feature: Checkout Process - End to End
  As a customer
  I want to complete the checkout process
  So that I can purchase the items in my cart

  Background:
    Given the Swag Labs app is installed and launched
    And I am on the login screen

  @regression
  Scenario Outline: Complete successful checkout flow
    When I login with username "<user_name>" and password "<user_password>"
    And I add "<product_1>" to the cart
    Then the cart badge should update to "1"

    When I add "<product_2>" to the cart
    Then the cart badge should update to "2"

    When I go to the "Checkout" screen
    And I fill checkout information with "<first_name>", "<last_name>", and "<zip_code>"
    Then I should navigate to the "Checkout: Overview" screen
    And I should see the products in the order list
    And I should see the order summary with Item Total, Tax, and Total

    When I tap the "Finish" button
    Then I should see an order confirmation popup
    And the popup should display "THANK YOU FOR YOU ORDER"

    Examples:
      | user_name     | user_password | product_1           | product_2             | first_name | last_name | zip_code |
      | standard_user | secret_sauce  | Sauce Labs Backpack | Sauce Labs Bike Light | John       | Doe       | 12345    |

  @regression @bug
  Scenario Outline: Checkout incomplete when removing all products during checkout
    When I login with username "<user_name>" and password "<user_password>"
    And I add "<product_1>" to the cart
    And I add "<product_2>" to the cart
    Then the cart badge should update to "2"

    When I go to the "Checkout" screen
    And I fill checkout information with "<first_name>", "<last_name>", and "<zip_code>"
    Then I should navigate to the "Checkout: Overview" screen
    And I should see the products in the order list
    And I should see the order summary with Item Total, Tax, and Total

    When I remove all products from checkout
    And I tap the "Finish" button
    Then I should see an incomplete order popup

    Examples:
      | user_name     | user_password | product_1           | product_2             | first_name | last_name | zip_code |
      | standard_user | secret_sauce  | Sauce Labs Backpack | Sauce Labs Bike Light | John       | Doe       | 12345    |

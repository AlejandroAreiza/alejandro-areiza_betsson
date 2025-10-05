# Swag Labs App - Test Cases

**Test scenarios in Gherkin syntax for automation implementation**

---

## TC-01: Login with Valid Credentials

**Feature:** User Authentication  
**Priority:** High (P1)  
**Risk Level:** Critical

### Scenario: Successful login with user credentials

```gherkin
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
```

---

## TC-02: Login with Invalid Credentials
**Feature:** User Authentication - Negative Testing  
**Priority:** High (P1)  
**Risk Level:** Critical

### Scenario: Failed login attempts with invalid credentials and users

```gherkin
Feature: User Authentication - Negative Scenarios
  As an invalid user
  I want to attempt login to the Swag Labs app
  So that the system validates and rejects my invalid credentials

  Background:
    Given the Swag Labs app is installed and launched
    And I am on the login screen

  Scenario Outline: Login attempt with invalid credentials
    When I login with username "<user_name>" and password "<user_password>"
    Then I should see an error message
    And the error message should contain "<error_text>"
    And I should remain on the login screen

    Examples:
      | user_name       | user_password | error_text                                                      |
      | invalid_user    | secret_sauce  | Username and password do not match any user in this service     |
      | standard_user   | wrong_pass    | Username and password do not match any user in this service     |
      | STANDARD_USER   | secret_sauce  | Username and password do not match any user in this service     |
      |    <empty>      | secret_sauce  | Username is required                                            |
      | standard_user   |    <empty>    | Password is required                                            |
      |    <empty>      |    <empty>    | Username is required                                            |
      | locked_out_user | secret_sauce  | Sorry, this user has been locked out                            |
```

---

## TC-03: Checkout Flow (End-to-End)
**Feature:** Checkout Process  
**Priority:** High (P1)  
**Risk Level:** Critical

### Scenario: Complete checkout with valid information

```gherkin
Feature: Checkout Process - End to End
  As a customer
  I want to complete the checkout process
  So that I can purchase the items in my cart

  Background:
    Given the Swag Labs app is installed and launched
    And I am on the login screen

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
    And the popup should display "THANK YOU FOR YOUR ORDER"

    When I close the confirmation popup
    Then the cart badge should show be empty
    And my cart should be empty

    Examples:
      | user_name     | user_password | product_1           | product_2             | first_name | last_name | zip_code |
      | standard_user | secret_sauce  | Sauce Labs Backpack | Sauce Labs Bike Light | John       | Doe       | 12345    |
      | problem_user  | secret_sauce  | Sauce Labs Backpack | Sauce Labs Bike Light | Jane       | Smith     | 90210    |
```

## TC-04: Checkout Flow (End-to-End)
### Scenario: Cannot complete checkout with no products

```gherkin
  Feature: Checkout Process - End to End
    As a customer
    I want to complete the checkout process
    So that I can purchase the items in my cart

    Background:
      Given the Swag Labs app is installed and launched
      And I am on the login screen
      
  Scenario Outline: Checkout fails when removing all products during checkout
    When I login with username "<user_name>" and password "<user_password>"
    And I add "<product_1>" to the cart
    And I add "<product2>" to the cart
    Then the cart badge should update to "2"

    When I go to the "Checkout" screen
    And I fill checkout information with "<first_name>", "<last_name>", and "<zip_code>"
    Then I should navigate to the "Checkout: Overview" screen
    And I should see the products in the order list
    And I should see the order summary with Item Total, Tax, and Total
    
    When I remove all products from checkout
    And I tap the "Finish" button
    Then I should see an order failed popup

    When I close the failed popup
    Then the cart badge should be empty
    And my cart should be empty

    Examples:
      | user_name     | user_password | product_1           | product_2           | first_name | last_name | zip_code |
      | standard_user | secret_sauce  | Sauce Labs Backpack | Sauce Labs Bike Light | John       | Doe       | 12345    |
```

---
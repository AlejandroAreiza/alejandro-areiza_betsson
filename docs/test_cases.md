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
      | user_name       | user_password | error_text                           |
      | invalid_user    | secret_sauce  | Username and password do not match   |
      | standard_user   | wrong_pass    | Username and password do not match   |
      | STANDARD_USER   | secret_sauce  | Username and password do not match   |
      |                 | secret_sauce  | Username is required                 |
      | standard_user   |               | Password is required                 |
      |                 |               | Username and password are required   |
      | locked_out_user | secret_sauce  | Sorry, this user has been locked out |
```

---

## TC-03: Add Multiple Products to Cart and Remove
**Feature:** Shopping Cart Management  
**Priority:** High (P1)  
**Risk Level:** High

### Scenario: Add and remove products from cart

```gherkin
Feature: Shopping Cart - Add and Remove Products
  As a registered user
  I want to add and remove products from my cart
  So that I can manage my purchases before checkout

  Background:
    Given the Swag Labs app is installed and launched
    And I am on the login screen

  Scenario Outline: Add multiple products and remove them from cart
    When I login with username "<user_name>" and password "<user_password>"
    And I add "<product_1>" to the cart
    Then the cart badge should update to "1"
    And the "Add to Cart" button for "<product_1>" should change to "Remove"
    
    When I add "<product_2>" to the cart
    Then the cart badge should update to "2"
    And the "Add to Cart" button for "<product_2>" should change to "Remove"
    
    When I add "<product_3>" to the cart
    Then the cart badge should update to "3"
    And the "Add to Cart" button for "<product_3>" should change to "Remove"
    
    When I tap the cart icon
    Then I should navigate to the "Your Cart" screen
    And I should see the added products in the cart
    
    When I swipe left on "<product_2>"
    Then "<product_2>" should be removed from the cart
    And the cart badge should update to "2"
    
    When I click on remove button from "<product_1>"
    Then "<product_1>" should be removed from the cart
    And the cart badge should update to "1"
    
    When I swipe left on "<product_3>"
    Then the cart should be empty
    And the cart badge should update to "0"

    Examples:
      | user_name     | user_password | product_1           | product_2             | product_3               |
      | standard_user | secret_sauce  | Sauce Labs Backpack | Sauce Labs Bike Light | Sauce Labs Bolt T-Shirt |
      | problem_user  | secret_sauce  | Sauce Labs Backpack | Sauce Labs Bike Light | Sauce Labs Bolt T-Shirt |
```

---

## TC-04: Complete Checkout Flow (End-to-End)
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
    Then the cart badge should show "0"
    And my cart should be empty

    Examples:
      | user_name     | user_password | product_1           | product_2             | first_name | last_name | zip_code |
      | standard_user | secret_sauce  | Sauce Labs Backpack | Sauce Labs Bike Light | John       | Doe       | 12345    |
      | problem_user  | secret_sauce  | Sauce Labs Backpack | Sauce Labs Bike Light | Jane       | Smith     | 90210    |


  Scenario Outline: Checkout fails when removing all products during checkout
    When I login with username "<user_name>" and password "<user_password>"
    And I add "<product_1>" to the cart
    Then the cart badge should update to "1"

    When I go to the "Checkout" screen
    And I fill checkout information with "<first_name>", "<last_name>", and "<zip_code>"
    Then I should navigate to the "Checkout: Overview" screen
    And I should see the products in the order list
    And I should see the order summary with Item Total, Tax, and Total
    
    When I remove all products from checkout
    And I tap the "Finish" button
    Then I should see an order failed popup

    When I close the failed popup
    Then the cart badge should show "0"
    And my cart should be empty

    Examples:
      | user_name     | user_password | product_1           | first_name | last_name | zip_code |
      | standard_user | secret_sauce  | Sauce Labs Backpack | John       | Doe       | 12345    |
```

---

## TC-05: Sort Products and Verify Order
**Feature:** Product Catalog - Sorting  
**Priority:** Medium (P2)  
**Risk Level:** Medium

### Scenario: Sort products by different criteria

```gherkin
Feature: Product Catalog - Sorting Functionality
  As a customer
  I want to sort products by different criteria
  So that I can easily find products based on my preferences

  Background:
    Given the Swag Labs app is installed and launched
    And I am on the login screen

  Scenario Outline: Sort products and verify the sorted order
    When I login with username "<user_name>" and password "<user_password>"
    And I tap the sort dropdown button
    And I select "<sort_option>" from the sort menu
    Then the products should be sorted by "<sort_criteria>" in "<order>" order
    And the first product should be "<first_product>"
    And the last product should be "<last_product>"

    When I change view
    Then the products should be sorted by "<sort_criteria>" in "<order>" order
    And the first product should be "<first_product>"
    And the last product should be "<last_product>"
    
    Examples:
      | user_name     | user_password | sort_option         | sort_criteria | order      | first_product        | last_product                |
      | standard_user | secret_sauce  | Name (Z to A)       | name          | descending | Test.allTheThings() T-Shirt | Sauce Labs Backpack  |
      | standard_user | secret_sauce  | Price (low to high) | price         | ascending  | Sauce Labs Onesie    | Sauce Labs Fleece Jacket    |
```

---
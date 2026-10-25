Feature: Add to cart functionality
  Scenario: User adds a product to the cart
    Given I am logged in on the inventory page
    When I add the product "Sauce Labs Backpack" to the cart
    Then I should see 1 item in the cart

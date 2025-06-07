Feature: Order Transaction
    Tests related to Order Transactions

  Scenario Outline: Verify Order success message shown in details page
    Given The user is on the login page
    And they login to portal with <username> and <password>
    When I place the item order with <username> and <password>
    And navigate to the Orders page
    And Select the OrderId
    Then Order message is successfully displayed
    Examples:
      | username        | password  |
      | smac7@gmail.com | Pic_appl1 |

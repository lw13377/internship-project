Feature: User can see out of stock items

  Scenario: filter out of stock
    Given Open sign in page
    And Type in Email
    Then Type in Password
    Then Log in to the page
    And Click on off plan option at the left side menu
    When Verify the right page opens
    And Filter by sale status to out of stock
    Then Verify each product contains the Out of Stocks tag
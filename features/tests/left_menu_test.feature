Feature: Testing from left meny bar


  Scenario: User can open the off plan page and go through the pagination
    Given Open sign in page
    And Type in Email
    Then Type in Password
    Then Log in to the page
    And Click on off plan option at the left side menu
    When Verify the right page opens
    Then Go to the final page using the pagination button
    And Go back to the first page using the pagination button

     Scenario: User can filter by Announced
    Given Open sign in page
    And Type in Email
    Then Type in Password
    Then Log in to the page
    And Click on off plan option at the left side menu
    When Verify the right page opens
    Then Filter by sale status of “Announced”.
    And Verify each product contains the Announced tag.
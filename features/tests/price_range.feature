Feature: Checking Price Range

  Scenario: User can filter 120k-200k price range
    Given Open sign in page
    And Type in Email
    Then Type in Password
    Then Log in to the page
    And Click on off plan option at the left side menu
    When Verify the right page opens
    Then Filter the range from 120k-200k
    And Verify all the results have the correct price range

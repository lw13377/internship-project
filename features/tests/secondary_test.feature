Feature: secondary

  Scenario: User can go to last page of secondary
    Given Open sign in page
    And Type in Email
    Then Type in Password
    Then Log in to the page
    And Open Secondary Page from the left
    When Verify that Secondary Page Opened
    Then Click on Next Page to the end
    And Click on Previous page to the end
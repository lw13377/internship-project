Feature: Settings

  Scenario: User can see all 12 settings
    Given Open sign in page
    And Type in Email
    Then Type in Password
    Then Log in to the page
    And Click on settings option
    When Verify the settings page opens
    Then Verify there are 12 options for the settings
    And Verify that connect the company button is available
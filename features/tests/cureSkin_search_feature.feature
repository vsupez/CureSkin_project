Feature: CureSkin Search Page feature

  Scenario: Top logo takes to the main page
    Given Open search results page Search: 18 results found for "cure"
    When  Click on CureSkin logo in the header
    Then Verify user is taken to the main page
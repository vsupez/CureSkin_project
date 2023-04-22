Feature: CureSkin Search Page feature

  Scenario: Top logo takes to the main page
    Given Open search results page Search: 18 results found for "cure"
    When  Click on CureSkin logo in the header
    Then Verify user is taken to the main page


  Scenario: User can verify UI elements on a Product Results Page
    Given Open the Cureskin Application
    When Search for facewash
    And  Click on the product from Search Results
    Then Verify UI elements present: image, price, reviews, quantity, add to cart, buy it now button









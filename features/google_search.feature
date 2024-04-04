Feature: testing google

  Scenario: visit google
    When we visit google
    Then it does have a title "Google"

  Scenario: Search for Twitter
    Given I am on the google home page
    When I search for twitter
    Then I see twitter in the search results

  Scenario: I visit Twitter from the search results
    Given I have searched for Twitter on google
    When I click on Twitter in the search results
    Then I am on the Twitter home page

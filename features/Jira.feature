Feature: testing Jira

Scenario: I can log in to Jira
  Given I am on the Jira login page
  When I enter in my username and password
  And I click the login button
  Then I am on logged in

Scenario: I can log out Jira
  Given I am logged in
  When I click to log out
  Then I am logged out
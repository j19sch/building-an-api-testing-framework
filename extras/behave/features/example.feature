# -- FILE: features/example.feature
Feature: Delete

  Scenario: Deleting a book
    Given we got all the books
      And we have valid credentials
    When we delete one book
    Then we get a 200 response
      And the book is no longer present
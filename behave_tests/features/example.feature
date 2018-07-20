# -- FILE: features/example.feature
Feature: getting stuff

  Scenario: Run a simple test
    Given we have posted an image
     When we retrieve the image
     Then we get both the existing and the newly posted image
Feature: Check that the following 10 scenarios pass

  Background:
    Given Home page: The user is on https://www.mega-image.ro/

  @regression
  Scenario: Check that the user can't create a new account if an invalid email format is provived
    When Home page: The user clicks on "Contul meu"
    When Login page: The user enters an invalid email and clicks "Continua"
    Then Login page: The user checks if the error for invalid email is displayed

  @regression
  Scenario: Check that the user can't create a new account if an invalid password is provided
    When Home page: The user clicks on "Contul meu"
    When Login page: The user enters a valid email and clicks "Continua"
    When Login page: The user enters an invalid password and clicks "Creeaza un cont nou"
    Then Login page: The user checks if the error for invalid password is displayed

  @regression
  Scenario: Check that the user can't create a new account without checking the "Terms and Conditions" checkbox
    When Home page: The user clicks on "Contul meu"
    When Login page: The user enters a valid email and clicks "Continua"
    When Login page: The user enters a valid password and clicks "Creeaza un cont nou"
    Then Login page: The user checks if the error for not checking "Terms and Conditions" is displayed

  @smoke
  Scenario: Check that the user can log in with existing credentials
    When Home page: The user clicks on "Contul meu"
    When Login page: The user enters an existing valid email and clicks "Continua"
    When Login page: The user enters a valid password and clicks "Autentificare"
    Then Home page: The user is logged in successfully

  @regression
  Scenario: Check if the user can make a search for a specific product on Home page
    When Home page: The user searches for "apa naturala 5l bucovina" in the search box
    Then Home page: The user found the item searched for

  @regression
  Scenario: Check if a product's double quantity's price is displayed correctly in shopping cart
    When Home page: The user searches for "apa naturala 5l bucovina" in the search box
    When Home page: The user adds one "Apa minerala naturala plata 5L" to shopping cart
    When Home page: The user navigates to shopping cart
    When Cart page: The user adds one extra "Apa minerala naturala plata 5L" in the shopping cart
    Then Cart page: The user checks if the total price is correctly displayed

  @regression
  Scenario: Check if a specific filter from "Cosmetice si ingrijire personala" is displaying the correct products
    When Home page: The user navigates to "Cosmetice si ingrijire personala"
    When Home page: The user checks the ">100RON" filter
    Then Home page: The user checks if all filtered products prices are over 100 RON

  @regression
  Scenario: Check that the user can remove the product/s from shopping cart
    When Home page: The user searches for "apa naturala 5l bucovina" in the search box
    When Home page: The user adds one "Apa minerala naturala plata 5L" to shopping cart
    When Home page: The user navigates to shopping cart
    When Cart page: The user removes the product from shopping cart
    Then Cart page: The user check if the shopping cart is empty

  @regression
  Scenario: Check that the sort in shopping cart for 3 products is correctly displayed
    When Home page: The user searches for "apa naturala 5l bucovina" and adds it to shopping cart
    When Home page: The user searches for "paine cu secara 400g Vita" and adds it to shopping cart
    When Home page: The user searches for "cascaval 350g desenvis", adds it and navigates to shopping cart
    When Cart page: The user sorts the products after "Pretul produsului"
    Then Cart page: The user checks if the products were sorted correctly

  @regression
  Scenario: Check that the total price of two products in shopping cart is correctly displayed
    When Home page: The user adds "Broasca testoasa", "Calut de mare" and navigates to shopping cart
    Then Cart page: The user check if the total price for the two products is correctly displayed
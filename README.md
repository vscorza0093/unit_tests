# unit_tests

Learning unit tests in Python, using pytest library


* Unit testing is a software testing method that focus on testing individual units of source code

* The main goal of this type of test is not to verify the work state at a specific moment, but to guarantee that nothing has broken and the application is fully working while it expand.


        pip install pytest
    

* We don't have to import any library to run pytest

        pytest unit_test.py

* But we have to name the test correctly on signature to our tests works
* The word "test" must come after any other charactere

        def sum(x, y):
            return x + y

        def test_sum():             |   def testsum():
            assert sum(x + y) == z  |       assert sum(x + y) == z

* The word keyword assert validate the test condition. Pytest show us a nice and legible log when we got error

## Test Driven Development

* Its a software development technique that treats about innovating faster and reducing waste. Coding the solutions throug the test development to understand the necessities of the final application

####* Better comprehension of functionality -> Starting by tests and not by the implementation to better understand the application and avoiding errors

####* Great system cover in a mutable environment -> Tests before code, thats the way to avoid great errors and handle with big system changes

####* Reliable to build up -> When working with TDD, all errors will be detected and corrected


* TDD is based on repetition cicle called Red-Green-Refactor, that needed to be followed

##### Red -> We have to code a test of a functionality that has not been implemented yet, knowing that it will fail, because of that.

##### Green -> The code already been implemented, so we execute the test again

##### Refactor -> Code improvement after all the test cases has passed


## Code covarage

        pip install pytest-cov

* We have to know all the functionaties embraced by the test coverage


# Unit Test Knowledge Sharing

## "The Reason"

* Automatically check each part ("Unit", a single class or a function) of your code is working as intended.

    * Positive / Negative Tests: Test if your code is able to handle both expected and unexpected inputs.

## How to use

* Requirements:
    * `pytest`
    * `pytest-cov`

* Usage

    * `pytest` # invoke under current directory
    * `pytest tests` # invoke only certain directory
    * `pytest tests/test_shopping_cart_1_assertion.py --cov=src/shopping --cov-report html -v` # invoke only certain test files, calculate the coverage against specific scripts, and generate coverage report HTML.


## Most Common Usage

* Assert

* Exception

* Fixture

* Parametrize

* Monkeypatch

## Coverage

* The reason

* Usage
    
* Calculation

* Report

## References:

* [How To Write Unit Tests in Python • Pytest Tutorial](https://www.youtube.com/watch?v=YbpKMIUjvK8)

* [Full pytest documentation](https://docs.pytest.org/en)
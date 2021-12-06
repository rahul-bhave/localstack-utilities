# LocalStack and pytest


## Prerequisites

* Python 3+
* Docker Compose

Install the required pip packages for the project with:

    $ pip3 install -r requirements.txt or pip install -r requirements.txt

## Run Localstack

The easy way is to run LocalStack with docker-compose

Run the LocalStack container in the background with:
    
    $ docker-compose up 


## Run test

A simple test that creates, invokes, and then tears down a simple Lambda is provided.

To run the test, use the following commands within the root of the project:

```
$ cd lambda
$ pytest -sv . 
```

Wait a while, you should see similar to the following:

```
$ pytest -sv
============================= test session starts =============================
platform win32 -- Python 3.9.6, pytest-5.3.5, py-1.11.0, pluggy-0.13.1 -- C:\Users\rahulbhave\code\localstack-utilities\venv3\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\rahulbhave\code\localstack-utilities\lambda
collecting ... collected 1 item

test_lambda.py::Test::test_that_lambda_returns_correct_message
Setting up the class
PASSED
Tearing down the class

---------printing test results------------
=== 1 passed and 0 failed tests in 16.08722424507141 seconds===
------------------------------------------

```
For writing tests in this repo following Medium article is refered:
https://medium.com/uk-hydrographic-office/developing-and-testing-lambdas-with-pytest-and-localstack-21a111b7f6e8

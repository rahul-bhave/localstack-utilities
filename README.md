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

This github action flow is very simple and consists of following three steps-

Step 1
Running localstack services.

```
name: Localstack CI
on: push
jobs:
  localstack:
    runs-on: ubuntu-latest
    services:
      localstack:
        image: localstack/localstack:latest
        env:
          SERVICES: lambda
          DEFAULT_REGION: eu-west-1
          AWS_ACCESS_KEY_ID: localkey
          AWS_SECRET_ACCESS_KEY: localsecret
        ports:
          - 4566:4566
          - 4571:4571

```

Step 2
Install python and other test dependencies

```
steps:
      - uses: actions/checkout@v2
      - name: Install Python 3.8
        uses: actions/setup-python@v1
        with:
          python-version: 3.8
      - name: Install dependencies
        run: |
          pip3 install --upgrade pip==20.0.1
          pip3 install -r requirements.txt
```

Step 3
Run the tests against LocalStack

```
# Execute Tests lambda
      - name: Run test for sample lambda
        run: |
          cd lambda
          pytest -sv
```

For writing tests in this repo following Medium article is refered:
https://medium.com/uk-hydrographic-office/developing-and-testing-lambdas-with-pytest-and-localstack-21a111b7f6e8

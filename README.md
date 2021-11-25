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
$ pytest -s . 
```

Wait a while, you should see similar to the following:

```
============================= test session starts =============================
platform win32 -- Python 3.9.6, pytest-5.3.5, py-1.11.0, pluggy-0.13.1
rootdir: C:\Users\rahulbhave\code\localstack-utilities\lambda
collected 1 item

test_lambda.py
Setting up the class
.
Tearing down the class

---------printing test results------------
=== 1 passed and 0 failed tests in 23.198726177215576 seconds===
------------------------------------------


============================= 1 passed in 23.21s ==============================

```
# https://github.com/ciaranevans/localstack_and_pytest_1

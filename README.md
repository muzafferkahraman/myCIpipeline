** My CI Pipeline with circleci **

myCIpipeline/
├── docs
│   ├── main.py
│   └── tests.py
├── Makefile
├── muzo.egg-info
│   ├── dependency_links.txt
│   ├── PKG-INFO
│   ├── SOURCES.txt
│   └── top_level.txt
├── README.md
├── requirements.txt
├── setup.py
├── src
│   ├── __init__.py
│   ├── main.py
│   └── __pycache__
│       └── main.cpython-36.pyc
└── tests
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-36.pyc
    │   └── tests.cpython-36.pyc
    └── tests.py




root@master myCIpipeline]# python3  tests/tests.py
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
[root@master myCIpipeline]# python3  tests/tests.py  -v
test_add (__main__.MyTestCase) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.000s

OK


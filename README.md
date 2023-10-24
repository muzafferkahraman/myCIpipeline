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



[root@master myCIpipeline]# ./Makefile
./Makefile: line 1: test:: command not found
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
./Makefile: line 4: build:: command not found
running install
/usr/local/lib/python3.6/site-packages/setuptools/command/install.py:37: SetuptoolsDeprecationWarning: setup.py install is deprecated. Use build and pip and other standards-based tools.
  setuptools.SetuptoolsDeprecationWarning,
/usr/local/lib/python3.6/site-packages/setuptools/command/easy_install.py:159: EasyInstallDeprecationWarning: easy_install command is deprecated. Use build and pip and other standards-based tools.
  EasyInstallDeprecationWarning,
running bdist_egg
running egg_info
writing muzo.egg-info/PKG-INFO
writing dependency_links to muzo.egg-info/dependency_links.txt
writing top-level names to muzo.egg-info/top_level.txt
reading manifest file 'muzo.egg-info/SOURCES.txt'
writing manifest file 'muzo.egg-info/SOURCES.txt'
installing library code to build/bdist.linux-x86_64/egg
running install_lib
running build_py
creating build
creating build/lib
creating build/lib/src
copying src/main.py -> build/lib/src
copying src/__init__.py -> build/lib/src
creating build/lib/tests
copying tests/__init__.py -> build/lib/tests
copying tests/tests.py -> build/lib/tests
creating build/bdist.linux-x86_64
creating build/bdist.linux-x86_64/egg
creating build/bdist.linux-x86_64/egg/src
copying build/lib/src/main.py -> build/bdist.linux-x86_64/egg/src
copying build/lib/src/__init__.py -> build/bdist.linux-x86_64/egg/src
creating build/bdist.linux-x86_64/egg/tests
copying build/lib/tests/__init__.py -> build/bdist.linux-x86_64/egg/tests
copying build/lib/tests/tests.py -> build/bdist.linux-x86_64/egg/tests
byte-compiling build/bdist.linux-x86_64/egg/src/main.py to main.cpython-36.pyc
byte-compiling build/bdist.linux-x86_64/egg/src/__init__.py to __init__.cpython-36.pyc
byte-compiling build/bdist.linux-x86_64/egg/tests/__init__.py to __init__.cpython-36.pyc
byte-compiling build/bdist.linux-x86_64/egg/tests/tests.py to tests.cpython-36.pyc
creating build/bdist.linux-x86_64/egg/EGG-INFO
copying muzo.egg-info/PKG-INFO -> build/bdist.linux-x86_64/egg/EGG-INFO
copying muzo.egg-info/SOURCES.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
copying muzo.egg-info/dependency_links.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
copying muzo.egg-info/top_level.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
zip_safe flag not set; analyzing archive contents...
creating dist
creating 'dist/muzo-0.1-py3.6.egg' and adding 'build/bdist.linux-x86_64/egg' to it
removing 'build/bdist.linux-x86_64/egg' (and everything under it)
Processing muzo-0.1-py3.6.egg
Copying muzo-0.1-py3.6.egg to /usr/local/lib/python3.6/site-packages
Removing muzo 0.1 from easy-install.pth file
Adding muzo 0.1 to easy-install.pth file

Installed /usr/local/lib/python3.6/site-packages/muzo-0.1-py3.6.egg
Processing dependencies for muzo==0.1
Finished processing dependencies for muzo==0.1


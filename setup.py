from distutils.core import setup
from setuptools import setup, find_packages

setup(
    name='muzo',
    version='0.1',
    author='muzokahraman',
    author_email='muzaffer.kahraman@outlook.com',
    packages=find_packages(),
    long_description=open('README.md').read()
)


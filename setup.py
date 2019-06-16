import os
from setuptools import setup

HERE = os.path.abspath(os.path.dirname(__file__))
README = os.path.join(HERE, "README.rst")

classifiers = [
    'License :: OSI Approved :: Apache Software License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Natural Language :: English',
    'Intended Audience :: Developers',
    'Intended Audience :: Information Technology',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
]

with open(README, 'r') as f:
    long_description = f.read()

setup(
    name='cheaders',
    version='1.0.0',
    description=('C file header generator'),
    long_description=long_description,
    url='http://github.com/eriknyquist/cheaders',
    author='Erik Nyquist',
    author_email='eknyquist@gmail.com',
    license='Apache 2.0',
    packages=['cheaders'],
    classifiers = classifiers,
)

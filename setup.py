"""Setup file for openworm-tests"""

import sys
from setuptools import setup
from pip.req import parse_requirements
from pip.download import PipSession

import os

def read_requirements():
    '''parses requirements from requirements.txt'''
    reqs_path = os.path.join('.', 'requirements.txt')
    install_reqs = parse_requirements(reqs_path, session=PipSession())
    reqs = [str(ir.req) for ir in install_reqs]
    return reqs

setup(
    name='owtests',
    version='0.01',
    author='OpenWorm developers & Rick Gekin',
    author_email='rgerkin@asu.edu',
    packages=['owtests'],
    url='http://www.openworm.org',
    license='MIT',
    description='Data-driven validation tests for the models that compose OpenWorm.',
    long_description="",  
    test_suite="owtests.unit_test",    
    install_requires=read_requirements(),
    entry_points={
        'console_scripts': [
            'owtests = owtests.__main__:main'
            ]
        }
    )




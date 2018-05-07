"""Setup file for openworm-tests"""
import sys
from setuptools import setup
import os

try:
    from pip.req import parse_requirements
    from pip.download import PipSession
except ImportError:
    from pip._internal.req import parse_requirements
    from pip._internal.download import PipSession

from setuptools import setup, find_packages

# IPython 6.0+ does not support Python 2.6, 2.7, 3.0, 3.1, or 3.2
if sys.version_info < (3,3):
    ipython = "ipython>=5.1,<6.0"
else:
    ipython = "ipython>=5.1"    

def read_requirements(url=False):
    '''parses requirements from requirements.txt'''
    reqs_path = os.path.join('.', 'requirements.txt')
    if url:
        with open(reqs_path) as f:
            reqs = [x.replace('-e ','') for x in f.read().split('\n')]
    else:
        install_reqs = parse_requirements(reqs_path, session=PipSession())
        reqs = [str(ir.req) for ir in install_reqs]
        reqs = [x.replace('-','==') for x in reqs]
    return reqs

setup(
    name='owtests',
    version='0.01',
    author='OpenWorm developers & Rick Gekin',
    author_email='rgerkin@asu.edu',
    packages=find_packages(),
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
        },
    dependency_links = read_requirements(url=True)
    )

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
    install_requires=['sciunit>=0.19',
                      'neuronunit>=0.19'],
    extras_require = {
        'channels':  ['channelworm>=0.1'],
        'cells': ['CElegansNeuroML>=0.4'],
        },
    entry_points={
        'console_scripts': [
            'owtests = owtests.__main__:main'
            ]
        },
    dependency_links = ["git+https://github.com/scidash/sciunit@dev#egg=sciunit-0.19",
                        "git+https://github.com/scidash/neuronunit@dev#egg=neuronunit-0.19",
                        "git+https://github.com/openworm/ChannelWorm@master#egg=channelworm-0.1",
                        "git+https://github.com/openworm/CElegansNeuroML@sciunit#egg=CElegansNeuroML-0.4"]
    )


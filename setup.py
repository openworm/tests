"""Setup file for openworm-tests"""
import sys
from setuptools import setup
import os

def read_requirements():
    '''parses requirements from requirements.txt'''
    reqs_path = os.path.join('.', 'requirements.txt')
    reqs = open(reqs_path, 'r')
    reqlist = [line.rstrip() for line in reqs]
    reqs.close()
    return reqlist

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
"""
Temporarily created versions on my fork which have the dependencies specified explicitly
"""

    dependency_links = ["git+https://github.com/gsarma/sciunit@pip10_workaround#egg=sciunit-0.19",
                        "git+https://github.com/gsarma/neuronunit@pip10_workaround#egg=neuronunit-0.19",
                        "git+https://github.com/openworm/ChannelWorm@master#egg=channelworm-0.1",
                        "git+https://github.com/openworm/CElegansNeuroML@sciunit#egg=CElegansNeuroML-0.4"]
    )

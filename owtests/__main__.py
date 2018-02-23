"""This module implements the OpenWorm Testing command line tools.
Examples to run from the command line:
owtest run
owtest run --buffer
"""

import sys
import os
import argparse
import sciunit
import unittest
from .unit_test import * # Import all unit test classes

import configparser
try:
    import matplotlib
    matplotlib.use('Agg') # Anticipate possible headless environments
except ImportError:
    pass

def main(*args):
    """The main routine."""
    parser = argparse.ArgumentParser()
    parser.add_argument("action", help="'run' to run the tests")
    parser.add_argument("--buffer", help="Buffer unit test output show only stdout/stderr from failing tests is displayed")
    args = parser.parse_args(args)
    if args.action == 'run': # If `owtest run` is executed...  
        unittest.main(buffer=args.buffer) # Run all the unit tests
    
if __name__ == '__main__':
    main()

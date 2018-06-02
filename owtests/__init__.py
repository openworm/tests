"""Validation tests for The Open Worm Project
------------------------------------------
This works best if it is installed first:
For normal users:
  pip install .
For developers:
  pip install -e . --process-dependency-links
Set an environment variable OW_HOME to the location of the directory
that contains any OpenWorm repositories that you want to test.
"""

import os
from sciunit.utils import NotebookTools
import unittest

DEFAULT_OW_HOME = os.path.join(os.environ.get('HOME'),'openworm')
OW_HOME = os.environ.get('OPENWORM_HOME',DEFAULT_OW_HOME)
if not os.path.isdir(OW_HOME):
    msg = 'No directory found at %s.  Please set OW_HOME to the location of your OpenWorm projects directory.' % OW_HOME
    raise FileNotFoundError(msg)
CW_HOME = os.path.join(OW_HOME,'ChannelWorm')

class ChannelNotebooks(NotebookTools,unittest.TestCase):
    """Unit tests for documentation notebooks"""

    path = 'ChannelWorm'

    # @unittest.skip("")
    # This is the original EGL-19 test that the others are based on
    def test_egl19a_iv(self):
        self.do_notebook('EGL-19a_CAEEL/EGL-19a_CAEEL')

    @unittest.skip("These are dummy tests.  Need to be filed out later")
    def test_egl2_CAEEL(self):
        self.do_notebook('EGL-2_CAEEL/EGL-2_CAEEL')

    @unittest.skip("These are dummy tests.  Need to be filed out later")
    def test_egl36_CAEEL(self):
        self.do_notebook('EGL-36_CAEEL/EGL-36_CAEEL')

    @unittest.skip("These are dummy tests.  Need to be filed out later")
    def test_exp2_CAEEL(self):
        self.do_notebook('EXP-2_CAEEL/EXP-2_CAEEL')

    @unittest.skip("These are dummy tests.  Need to be filed out later")
    def test_kqt1_CAEEL(self):
        self.do_notebook('kqt-1_CAEEL/kqt-1_CAEEL')

    @unittest.skip("These are dummy tests.  Need to be filed out later")
    def test_kqt3_CAEEL(self):
        self.do_notebook('kqt-3_CAEEL/kqt-3_CAEEL')

    @unittest.skip("These are dummy tests.  Need to be filed out later")
    def test_shk1a_CAEEL(self):
        self.do_notebook('SHK-1a_CAEEL/SHK-1a_CAEEL')

    @unittest.skip("These are dummy tests.  Need to be filed out later")
    def test_shl1_CAEEL(self):
        self.do_notebook('SHL-1_CAEEL/SHL-1_CAEEL')

    @unittest.skip("These are dummy tests.  Need to be filed out later")
    def test_slo1a_CAEEL(self):
        self.do_notebook('SLO-1a_CAEEL/SLO-1a_CAEEL')

    @unittest.skip("These are dummy tests.  Need to be filed out later")
    def test_slo2b_CAEEL(self):
        self.do_notebook('SLO-2b_CAEEL/SLO-2b_CAEEL')

    @unittest.skip("These are dummy tests.  Need to be filed out later")
    def test_slo2c_CAEEL(self):
        self.do_notebook('SLO-2c_CAEEL/SLO-2c_CAEEL')

    @unittest.skip("These are dummy tests.  Need to be filed out later")
    def test_twk18_CAEEL(self):
        self.do_notebook('TWK18_CAEEL/TWK18_CAEEL')

class CellNotebooks(NotebookTools,unittest.TestCase):
    """Unit tests for documentation notebooks"""

    # Path to testing notebooks
    path = 'CElegansNeuroML'

    # @unittest.skip("for development purposes")
    def test_muscle_model(self):
        self.do_notebook('Muscle-Model')

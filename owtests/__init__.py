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

    """
    If the path is the same for all tests in a class, use
    the variable path.  Otherwise, the two argument form of
    do_notebook accepts the path relative to owtests as the
    first argument and the notebook name as the second.
    """
    path = ''

    # This can probably be removed, but I wanted Rick to look at the changes first
    def test_egl19_iv(self):
        self.do_notebook(['ChannelWorm','EGL-19_IV'])

    @unittest.skip("These are dummy tests.  Need to be filed out later")
    def test_egl19a_iv(self):
        self.do_notebook(['ChannelWorm/EGL-19a_CAEEL','EGL-19a_CAEEL'])

    @unittest.skip("These are dummy tests.  Need to be filed out later")
    def test_egl2_CAEEL(self):
        self.do_notebook(['ChannelWorm/EGL-2_CAEEL','EGL-2_CAEEL'])

    @unittest.skip("These are dummy tests.  Need to be filed out later")
    def test_egl36_CAEEL(self):
        self.do_notebook(['ChannelWorm/EGL-36_CAEEL','EGL-36_CAEEL'])

    @unittest.skip("These are dummy tests.  Need to be filed out later")
    def test_exp2_CAEEL(self):
        self.do_notebook(['ChannelWorm/EXP-2_CAEEL','EXP-2_CAEEL'])

    @unittest.skip("These are dummy tests.  Need to be filed out later")
    def test_kqt1_CAEEL(self):
        self.do_notebook(['ChannelWorm/kqt-1_CAEEL','kqt-1_CAEEL'])

    @unittest.skip("These are dummy tests.  Need to be filed out later")
    def test_kqt3_CAEEL(self):
        self.do_notebook(['ChannelWorm/kqt-3_CAEEL','kqt-3_CAEEL'])

    @unittest.skip("These are dummy tests.  Need to be filed out later")
    def test_shk1a_CAEEL(self):
        self.do_notebook(['ChannelWorm/SHK-1a_CAEEL','SHK-1a_CAEEL'])

    @unittest.skip("These are dummy tests.  Need to be filed out later")
    def test_shl1_CAEEL(self):
        self.do_notebook(['ChannelWorm/SHL-1_CAEEL','SHL-1_CAEEL'])

    @unittest.skip("These are dummy tests.  Need to be filed out later")
    def test_slo1a_CAEEL(self):
        self.do_notebook(['ChannelWorm/SLO-1a_CAEEL','SLO-1a_CAEEL'])

    @unittest.skip("These are dummy tests.  Need to be filed out later")
    def test_slo2b_CAEEL(self):
        self.do_notebook(['ChannelWorm/SLO-2b_CAEEL','SLO-2b_CAEEL'])

    @unittest.skip("These are dummy tests.  Need to be filed out later")
    def test_slo2c_CAEEL(self):
        self.do_notebook(['ChannelWorm/SLO-2c_CAEEL','SLO-2c_CAEEL'])

    @unittest.skip("These are dummy tests.  Need to be filed out later")
    def test_twk18_CAEEL(self):
        self.do_notebook(['ChannelWorm/TWK18_CAEEL','TWK18_CAEEL'])

class CellNotebooks(NotebookTools,unittest.TestCase):
    """Unit tests for documentation notebooks"""

    # Path to testing notebooks.  Use if all notebooks in this class
    # share a path
    path = 'CElegansNeuroML'

    # @unittest.skip("for development purposes")
    def test_muscle_model(self):
        self.do_notebook('Muscle-Model')

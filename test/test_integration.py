import unittest
import os
import sys
import threading
import time

from pathlib import Path as path

TEST_DIR = os.path.dirname(__file__)
sys.path.append(os.path.abspath(
    os.path.normpath(os.path.join(TEST_DIR, '../src'))))

class IntegrationTest(unittest.TestCase):
    base_path = None

    def setUp(self):
        self.base_path = path(__file__).absolute().parent.parent
        mockup_path = self.base_path / "src" / "mock"

        sys.path.append(os.fspath(mockup_path))

    def tearDown(self):
        pass

    def testMinimalUseCase(self):
        import main
        main.main()

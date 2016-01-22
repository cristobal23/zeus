"""Testing utilities for Zeus."""

from zeus.cli.main import MyCLITestApp
from cement.utils.test import *

class MyCLITestCase(CementTestCase):
    app_class = MyCLITestApp

    def setUp(self):
        """Override setup actions (for every test)."""
        super(MyCLITestCase, self).setUp()

    def tearDown(self):
        """Override teardown actions (for every test)."""
        super(MyCLITestCase, self).tearDown()


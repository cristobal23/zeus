"""CLI tests for zeus."""

from zeus.utils import test

class CliTestCase(test.MyCLITestCase):
    def test_zeus_cli(self):
        self.app.setup()
        self.app.run()
        self.app.close()

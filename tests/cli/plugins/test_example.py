"""Tests for Example Plugin."""

from zeus.utils import test

class ExamplePluginTestCase(test.MyCLITestCase):
    def test_load_example_plugin(self):
        self.app.setup()
        self.app.plugin.load_plugin('example')

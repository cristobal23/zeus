"""Zeus bootstrapping."""

# All built-in application controllers should be imported, and registered
# in this file in the same way as MyCLIBaseController.

from cement.core import handler
from zeus.cli.controllers.base import MyCLIBaseController

def load(app):
    handler.register(MyCLIBaseController)

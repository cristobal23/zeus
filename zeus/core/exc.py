"""Zeus exception classes."""

class MyCLIError(Exception):
    """Generic errors."""
    def __init__(self, msg):
        Exception.__init__(self)
        self.msg = msg

    def __str__(self):
        return self.msg

class MyCLIConfigError(MyCLIError):
    """Config related errors."""
    pass

class MyCLIRuntimeError(MyCLIError):
    """Generic runtime errors."""
    pass

class MyCLIArgumentError(MyCLIError):
    """Argument related errors."""
    pass

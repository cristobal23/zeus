"""Zeus main application entry point."""

from cement.core.foundation import CementApp
from cement.utils.misc import init_defaults
from cement.core.exc import FrameworkError, CaughtSignal
from zeus.core import exc

# Application default.  Should update config/zeus.conf to reflect any
# changes, or additions here.
defaults = init_defaults('zeus')

# All internal/external plugin configurations are loaded from here
defaults['zeus']['plugin_config_dir'] = '/etc/zeus/plugins.d'

# External plugins (generally, do not ship with application code)
defaults['zeus']['plugin_dir'] = '/var/lib/zeus/plugins'

# External templates (generally, do not ship with application code)
defaults['zeus']['template_dir'] = '/var/lib/zeus/templates'


class MyCLIApp(CementApp):
    class Meta:
        label = 'zeus'
        config_defaults = defaults

        # All built-in application bootstrapping (always run)
        bootstrap = 'zeus.cli.bootstrap'

        # Internal plugins (ship with application code)
        plugin_bootstrap = 'zeus.cli.plugins'

        # Internal templates (ship with application code)
        template_module = 'zeus.cli.templates'


class MyCLITestApp(MyCLIApp):
    """A test app that is better suited for testing."""
    class Meta:
        # default argv to empty (don't use sys.argv)
        argv = []

        # don't look for config files (could break tests)
        config_files = []

        # don't call sys.exit() when app.close() is called in tests
        exit_on_close = False


# Define the applicaiton object outside of main, as some libraries might wish
# to import it as a global (rather than passing it into another class/func)
app = MyCLIApp()

def main():
    with app:
        try:
            app.run()
        
        except exc.MyCLIError as e:
            # Catch our application errors and exit 1 (error)
            print('MyCLIError > %s' % e)
            app.exit_code = 1
            
        except FrameworkError as e:
            # Catch framework errors and exit 1 (error)
            print('FrameworkError > %s' % e)
            app.exit_code = 1
            
        except CaughtSignal as e:
            # Default Cement signals are SIGINT and SIGTERM, exit 0 (non-error)
            print('CaughtSignal > %s' % e)
            app.exit_code = 0


if __name__ == '__main__':
    main()

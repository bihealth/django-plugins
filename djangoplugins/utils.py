from importlib import import_module
import sys

from django.conf import settings
from django.db import connection
from django.urls import include, re_path


def get_plugin_name(cls):
    return "%s.%s" % (cls.__module__, cls.__name__)


def get_plugin_from_string(plugin_name):
    """
    Returns plugin or plugin point class from given ``plugin_name`` string.

    Example of ``plugin_name``::

        'my_app.MyPlugin'

    """
    modulename, classname = plugin_name.rsplit(".", 1)
    module = import_module(modulename)
    return getattr(module, classname)


def include_plugins(point, pattern=r"{plugin}/", urls="urls"):
    # This hack allows us to run a syncplugins without including plugins in urls.
    if sys.argv[0] == "manage.py" and sys.argv[1] in ("migrate", "makemigration"):
        return include([])

    pluginurls = []
    for plugin in point.get_plugins():
        if hasattr(plugin, urls) and hasattr(plugin, "name"):
            _urls = getattr(plugin, urls)
            for _url in _urls:
                _url.default_args["plugin"] = plugin.name
            pluginurls.append(re_path(pattern.format(plugin=plugin.name), include(_urls)))
    return include(pluginurls)


def import_app(app_name):
    try:
        mod = import_module(app_name)
    except ImportError:  # Maybe it's AppConfig
        parts = app_name.split(".")
        tmp_app, app_cfg_name = ".".join(parts[:-1]), parts[-1]
        try:
            tmp_app = import_module(tmp_app)
        except ImportError:
            raise
        mod = getattr(tmp_app, app_cfg_name).name

        # Workaround for not finding app plugins modules in all cases
        try:
            mod = import_module("{}.plugins".format(mod))
        except ImportError:
            pass

    return mod


def load_plugins():
    for app in settings.INSTALLED_APPS:
        try:
            import_module("%s.plugins" % app)
        except ImportError:
            import_app(app)


def db_table_exists(table_name):
    return table_name in connection.introspection.table_names()

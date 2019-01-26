from .archive import BookstoreContentsArchiver
from .bookstore_config import BookstoreSettings
from .handlers import load_jupyter_server_extension
from ._version import get_versions


__version__ = get_versions()['version']
del get_versions


def _jupyter_server_extension_paths():
    return [dict(module="bookstore")]

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

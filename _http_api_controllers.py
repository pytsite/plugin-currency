"""PytSite Currency Plugin  HTTP API
"""
__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from pytsite import routing as _routing
from . import _api


class GetList(_routing.Controller):
    def exec(self) -> dict:
        """Get currencies list.
        """
        r = {}
        for c in _api.get_all():
            if c.startswith('_'):
                continue

            r[c] = {
                'title': _api.get_title(c),
                'symbol': _api.get_symbol(c),
            }

        return r

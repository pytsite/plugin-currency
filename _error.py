"""PytSite Currency Plugin Errors
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


class NoCurrenciesDefined(Exception):
    pass


class CurrencyNotDefined(Exception):
    pass


class CurrencyAlreadyDefined(Exception):
    pass

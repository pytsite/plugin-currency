"""PytSite Currency Plugin
"""
# Public API
from . import _model as model
from ._api import define, get_all, get_main, set_main, get_rate, exchange, fmt, get_title, get_symbol
from . import _widget as widget, _error as error

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def _init():
    """Init wrapper.
    """
    from pytsite import reg, tpl, lang, router, events
    from plugins import permissions, odm, admin, http_api
    from . import _api, _model, _eh, _http_api_controllers

    # Permission group
    permissions.define_group('currency', 'currency@currency')

    # Language package
    lang.register_package(__name__)

    # Loading currencies from registry config
    for code in reg.get('currency.list', ('USD',)):
        _api.define(code)

    # Tpl globals
    tpl.register_global('currency_fmt', _api.fmt)

    # ODM models
    odm.register_model('currency_rate', model.Rate)

    # Admin menu
    admin.sidebar.add_section('currency', 'currency@currency', 260)
    admin.sidebar.add_menu(
        'currency',
        'rates',
        'currency@rates',
        router.rule_path('odm_ui@browse', {'model': 'currency_rate'}),
        'fa fa-usd',
        weight=10,
        permissions=(
            'odm_auth.create.currency_rate',
            'odm_auth.modify.currency_rate',
            'odm_auth.delete.currency_rate',
        )
    )

    # Event handlers
    events.listen('odm.model.user.setup_fields', _eh.odm_model_user_setup)
    events.listen('odm_ui.user.m_form_setup_widgets', _eh.odm_ui_user_m_form_setup_widgets)
    events.listen('auth.http_api.get_user', _eh.auth_http_api_get_user)

    # HTTP API handlers
    http_api.handle('GET', 'currency/list', _http_api_controllers.GetList, 'currency@get_list')


# Package initialization
_init()

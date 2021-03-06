"""PytSite Currency Plugin  Event Handlers
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from pytsite import lang as _lang
from plugins import widget as _widget, form as _form, auth as _auth, odm as _odm, auth_storage_odm as _auth_storage_odm
from . import _widget as _currency_widget, _api


def odm_model_user_setup(entity: _auth_storage_odm.model.ODMUser):
    entity.define_field(_odm.field.String('currency', default=_api.get_main()))


def odm_ui_user_m_form_setup_widgets(frm: _form.Form, entity: _auth_storage_odm.model.ODMUser):
    cnt_wrapper = frm.get_widget('content-wrapper')  # type: _widget.container.Container
    cnt_wrapper.append_child(_currency_widget.Select(
        uid='currency',
        weight=105,
        label=_lang.t('currency@currency'),
        value=entity.f_get('currency'),
        h_size='col-xs-12 col-sm-6 col-md-5 col-lg-4',
        required=True,
    ))


def auth_http_api_get_user(user: _auth.model.AbstractUser, json: dict):
    if not isinstance(user, _auth_storage_odm.model.User):
        return

    c_user = _auth.get_current_user()
    if c_user == user or c_user.is_admin:
        json['currency'] = user.get_field('currency')

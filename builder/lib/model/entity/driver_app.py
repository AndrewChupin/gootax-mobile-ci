# Author Andrew Chupin
# Coding in UTF-8
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Column

from backend.model.entity.app import Application


class DriverApplication:

    def __init__(self, id: int =0, app_name='', bundle='', tenant_name='', host='',
                 new_host='', chat_host='', geocode_host='', push_key='', google_map_key='', app_type='',
                 version_app='', use_sms_auth='',
                 use_worker_reg='', worker_reg_url='', worker_reg_description='', worker_reg_button=''):
        self.id: int = id
        self.app_name = app_name
        self.bundle = bundle
        self.tenant_name = tenant_name
        self.host = host
        self.new_host = new_host
        self.chat_host = chat_host
        self.geocode_host = geocode_host
        self.push_key = push_key
        self.google_map_key = google_map_key
        self.app_type = app_type
        self.version_app = version_app
        self.status = Application.STATUS_BASE

        self.use_worker_reg = use_worker_reg
        self.worker_reg_url = worker_reg_url
        self.worker_reg_description = worker_reg_description
        self.worker_reg_button = worker_reg_button
        self.use_sms_auth = use_sms_auth




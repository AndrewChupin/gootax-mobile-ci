# Author Andrew Chupin
# Coding in UTF-8
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, Boolean
from sqlalchemy import String
from sqlalchemy import Column

from backend.model.entity.app import Application


'''
Конфигурируем:

- Тенант_домен (Домен не ИД)(Домен не ИД)

- Код версии
- Название версии

- Ключ для карты гугл
- Ключ для пушей

- Картинки
- JSON для пушей
'''

Base = declarative_base()
table_name = "driver_app_new"


class DriverApplicationNew(Base):
    __tablename__ = table_name

    STATUS_BASE = 0
    STATUS_CREATED = 1
    STATUS_WAITING = 2
    STATUS_EXECUTING = 3
    STATUS_SUCCESS = 4
    STATUS_ERROR = 5

    id = Column(Integer, primary_key=True)
    app_name = Column(String)
    bundle = Column(String, unique=True)
    tenant_name = Column(String, unique=True)

    host = Column(String)
    new_host = Column(String)
    chat_host = Column(String)
    geocode_host = Column(String)
    push_key = Column(String)
    google_map_key = Column(String)
    app_type = Column(Integer)
    version_app = Column(Integer)
    allow_root = Column(Boolean)
    yandex_key = Column(String)

    use_worker_reg = Column(Boolean)
    use_sms_auth = Column(Boolean)
    worker_reg_url = Column(String)
    worker_reg_description = Column(String)
    worker_reg_button = Column(String)

    status = Column(Integer, nullable=False)


    def __init__(self, app_name='', bundle='', tenant_name='', host='',
                 new_host='', chat_host='', geocode_host='', push_key='', google_map_key='', app_type='',
                 allow_root='', yandex_key='', use_sms_auth='',
                 version_app='', use_worker_reg='', worker_reg_url='', worker_reg_description='', worker_reg_button=''):
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
        self.allow_root = allow_root
        self.yandex_key = yandex_key
        self.status = Application.STATUS_BASE

        self.use_sms_auth = use_sms_auth
        self.use_worker_reg = use_worker_reg
        self.worker_reg_url = worker_reg_url
        self.worker_reg_description = worker_reg_description
        self.worker_reg_button = worker_reg_button


    def dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


# Author Andrew Chupin
# Coding in UTF-8
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, Boolean
from sqlalchemy import String
from sqlalchemy import Column

from backend.model.entity.app import Application


Base = declarative_base()
table_name = "build_config"


class BuildConfig(Base):
    __tablename__ = table_name

    id = Column(Integer, primary_key=True)
    app_id = Column(Integer, unique=True)
    build_type = Column(String)
    build_market = Column(Boolean)
    create_app = Column(Boolean)
    email = Column(String)
    version_code = Column(Integer)
    version_name = Column(String)
    ios_company_name = Column(String)
    branch = Column(String)
    build_email = Column(String)
    company_id = Column(Integer)


    def __init__(self, app_id = '', build_type='', build_market='', create_app='', email='',
                 version_code='', version_name='', ios_company_name='', branch='', build_email='', company_id=''):
        self.app_id = app_id
        self.build_type = build_type
        self.build_market = build_market
        self.create_app = create_app
        self.email = email
        self.version_code = version_code
        self.version_name = version_name
        self.ios_company_name = ios_company_name
        self.branch = branch
        self.build_email = build_email
        self.company_id = company_id


    def dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


import logging
import traceback

import pymysql
from pymysql import IntegrityError
from sqlalchemy import create_engine
from sqlalchemy import desc
from sqlalchemy.orm import sessionmaker

from backend.model.entity.build_config import BuildConfig


pymysql.install_as_MySQLdb()


class BuildConfigRepository:
    def __init__(self, url: str):
        engine = create_engine(url, encoding='utf8')
        self.Session = sessionmaker(bind=engine)


    def get_all_apps(self):
        session = self.Session()
        try:
            apps = session.query(BuildConfig).order_by(desc(BuildConfig.id)).all()
        except:
            traceback.print_exc()
            raise
        finally:
            session.close()
        return apps


    def get_all_desc(self):
        session = self.Session()
        try:
            apps = session.query(BuildConfig).order_by(desc(BuildConfig.id)).all()
            result = [dict(app.dict()) for app in apps]
        except:
            traceback.print_exc()
            raise
        finally:
            session.close()
        logging.info(result)
        return result


    def get_by_id(self, index: int) -> BuildConfig:
        session = self.Session()
        try:
            app = session.query(BuildConfig).filter_by(id=index).first()
        except:
            traceback.print_exc()
            raise
        finally:
            session.close()
        return app


    def get_by_app_id(self, index: int) -> BuildConfig:
        session = self.Session()
        try:
            app = session.query(BuildConfig).filter_by(app_id=index).first()
        except:
            traceback.print_exc()
            raise
        finally:
            session.close()
        return app


    def get_by_id(self, index: int) -> BuildConfig:
        session = self.Session()
        try:
            app = session.query(BuildConfig).filter_by(id=index).first()
        except:
            traceback.print_exc()
            raise
        finally:
            session.close()
        return app

    def update(self, app: BuildConfig) -> bool:
        session = self.Session()
        try:
            session.merge(app)
            session.commit()
        except:
            session.rollback()
            traceback.print_exc()
        finally:
            session.close()
        return True


    def create(self, app: BuildConfig) -> bool:
        session = self.Session()
        try:
            session.add(app)
            session.commit()
        except IntegrityError as e:
            session.rollback()
            traceback.print_exc()
            raise e
        finally:
            session.close()
        return True



    def delete(self, app: BuildConfig) -> bool:
        session = self.Session()
        try:
            session.delete(app)
            session.commit()
        except:
            session.rollback()
            traceback.print_exc()
        finally:
            session.close()
        return True

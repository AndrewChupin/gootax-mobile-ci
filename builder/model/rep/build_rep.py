import logging
import traceback

import pymysql
from pymysql import IntegrityError
from sqlalchemy import create_engine
from sqlalchemy import desc
from sqlalchemy.orm import sessionmaker

from builder.model.entity.build import Build

pymysql.install_as_MySQLdb()


class BuildRepository:

    def __init__(self, url: str):
        engine = create_engine(url, encoding='utf8')
        self.Session = sessionmaker(bind=engine)


    def get_all_builds(self):
        session = self.Session()
        try:
            builds = session.query(Build).order_by(desc(Build.id)).all()
        except:
            traceback.print_exc()
            raise
        finally:
            session.close()
        return builds


    def get_all_builds_desc(self):
        session = self.Session()
        try:
            builds = session.query(Build).order_by(desc(Build.id)).all()
            result = [dict(build.dict()) for build in builds]
        except:
            traceback.print_exc()
            raise
        finally:
            session.close()
        logging.info(result)
        return result


    def get_build_by_id(self, index: int) -> Build:
        session = self.Session()
        try:
            build = session.query(Build).filter_by(id=index).first()
        except:
            traceback.print_exc()
            raise
        finally:
            session.close()
        return build


    def update_build(self, build: Build) -> bool:
        session = self.Session()
        try:
            session.merge(build)
            session.commit()
        except:
            session.rollback()
            traceback.print_exc()
        finally:
            session.close()
        return True


    def create_build(self, build: Build) -> bool:
        session = self.Session()
        try:
            session.add(build)
            session.commit()
        except IntegrityError as e:
            session.rollback()
            traceback.print_exc()
            raise e
        finally:
            session.close()
        return True


    def update_build_state(self, build: Build) -> bool:
        session = self.Session()
        try:
            session.merge(build)
            session.commit()
        except:
            session.rollback()
            traceback.print_exc()
        finally:
            session.close()
        return True


    def delete_build(self, build: Build) -> bool:
        session = self.Session()
        try:
            session.delete(build)
            session.commit()
        except:
            session.rollback()
            traceback.print_exc()
        finally:
            session.close()
        return True

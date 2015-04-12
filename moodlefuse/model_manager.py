from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

session = None


def setup_model(database_file):
    global session
    engine = create_engine(database_file)
    s = sessionmaker()
    s.configure(bind=engine)
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)
    session = s()


class Service(object):
    __model__ = None

    def _isinstance(self, model, raise_error=True):
        valid_type = isinstance(model, self.__model__)
        if not valid_type and raise_error:
            raise ValueError('%s is not of type %s' % (model, self.__model__))
        return valid_type

    def save(self, model):
        self._isinstance(model)
        session.add(model)
        session.commit()
        return model

    def create(self, **kwargs):
        return self.save(self.__model__(**kwargs))

    def delete(self, model):
        self._isinstance(model)
        session.delete(model)
        session.commit()

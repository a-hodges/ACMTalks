import time
from contextlib import contextmanager

@contextmanager
def sqlalchemy_context(Session, autocommit=False):
    '''
    Creates a context for a sqlalchemy session
    '''
    session = Session(autocommit=autocommit)
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


class SQLAlchemyContext:
    '''
    Refactored version of the sqlalchemy_context
    '''
    def __init__(self, Session, autocommit=False):
        self.Session = Session
        self.autocommit = autocommit

    def __enter__(self):
        self.session = self.Session(autocommit=self.autocommit)
        return self.session

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            self.ession.rollback()
        else:
            self.session.commit()
        self.session.close()
        self.session = None


@contextmanager
def timeit(name='Timer'):
    '''
    Timing context manager
    Times whatever it wraps
    '''
    tstart = time.time()
    yield
    tend = time.time()
    print('{} took {:.3f} seconds'.format(name, tend - tstart))

with timeit('Sleep'):  # used as a normal context
    time.sleep(1)


@timeit('Wait')  # used as a context decorator
def wait(t):
    time.sleep(t)

wait(1)

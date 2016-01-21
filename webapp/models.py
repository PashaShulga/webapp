from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    String,
    DateTime,
    Numeric,
    ForeignKey,
    Boolean
    )

from sqlalchemy.sql import func

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    relationship
    )

from zope.sqlalchemy import ZopeTransactionExtension

from pyramid.security import (
    Allow,
    Everyone
    )

from passlib.apps import custom_app_context as blogger_pwd_context

import datetime

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    mail = Column(String(50))
    password = Column(String(512))
    sex = Column(String(10))
    is_active = Column(Boolean(), default=False)
    activate_code = Column(String(512))

    def verify_password(self, password):
        # is it cleartext?
        if password == self.password:
            self.set_password(password)

        return blogger_pwd_context.verify(password, self.password)

    def set_password(self, password):
        password_hash = blogger_pwd_context.encrypt(password)
        self.password = password_hash
        # return self.password


class Charity(Base):
    __tablename__ = 'charity'
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    logo = Column(String(128), nullable=True)
    description = Column(Text)
    bundle = relationship("Bundle", uselist=False, backref="charity")

    # def __init__(self, name=None, logo=None, description=None):
    #     self.name = name
    #     self.logo = logo
    #     self.description = description
    #
    # def __repr__(self):
    #     return "<Charity(%s, %s, %s)>" % (self.name, self.logo, self.description)


class Bundle(Base):
    __tablename__ = 'bundle'
    id = Column(Integer, primary_key=True)
    title = Column(String(256))
    description = Column(Text)
    date_start = Column(DateTime, nullable=True)
    date_end = Column(DateTime, nullable=True)
    charity_id = Column(Integer, ForeignKey(Charity.id))

    # def __init__(self, title=None, description=None, date_start=None, date_end=None):
    #     self.title = title
    #     self.description = description
    #     self.date_start = date_start
    #     self.date_end = date_end
    #
    # def __repr__(self):
    #     return "<Bundle(%s, %s, %s, %s)>" % (self.title, self.description, self.date_end, self.date_start)


class Content(Base):
    __tablename__ = 'content'
    id = Column(Integer, primary_key=True)
    title = Column(String(256))
    description = Column(Text)
    manufacture = Column(String(50))
    link = Column(String(100))
    image = Column(String(100))
    tier = Column(Numeric(precision=5, scale=4))
    bundle_id = Column(Integer, ForeignKey(Bundle.id))

    # def __init__(self, title=None, description=None, manufacture=None, link=None, image=None):
    #     self.title = title
    #     self.description = description
    #     self.manufacture = manufacture
    #     self.link = link
    #     self.image = image
    #
    # def __repr__(self):
    #     return "<Content(%s, %s, %s, %s, %s)>" % (self.title, self.description, self.manufacture, self.link, self.image)


class RootFactory(object):
    __acl__ = [(Allow, Everyone, 'view'),
               (Allow, 'group:editors', 'edit')
               ]
    def __init__(self, request):
        pass


class Orders(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    sum_content = Column(Numeric(precision=5, scale=4))
    sum_charity = Column(Numeric(precision=5, scale=4))
    bundle_id = Column(Integer, ForeignKey(Bundle.id))
    timestamp = Column(DateTime, default=datetime.datetime.utcnow())
    mail = Column(String(50))

    def __init__(self, sum_content=None, sum_charity=None, bundle_id=None, timestamp=datetime.datetime.utcnow(), mail=None):
        self.sum_content = sum_content
        self.sum_charity = sum_charity
        self.timestamp = timestamp
        self.bundle_id = bundle_id
        self.mail = mail

    # def __repr__(self):
    #     return "<Orders(%s, %s, %s)>" % (self.sum_offer, self.timestamp, self.content)
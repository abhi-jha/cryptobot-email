#!/usr/bin/env python

import string
from passlib.hash import sha1_crypt
from random import SystemRandom
from sqlalchemy import MetaData, Table, Column, String, ForeignKey, create_engine, Integer
from sqlalchemy.orm import mapper, relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import OperationalError, ProgrammingError
SQLAlchemyBase = declarative_base()

class BlockedEmail(SQLAlchemyBase):
  __tablename__ = 'unsubscribe'
  hashed_address = Column(String, primary_key=True)

  def __init__(self, hashed_address):
    self.hashed_address = hashed_address

class Hash(SQLAlchemyBase):
  __tablename__ = 'hash'
  uid = Column(Integer, primary_key=True)
  salt = Column(String)
  rounds = Column(Integer)
  name = Column(String) # just for reference

  def __init__(self, salt, rounds, name='SHA1'):
    self.salt = salt
    self.rounds = rounds
    self.name = name


class Database():
  def __init__(self, url, setup=False, debug=False):
    self.engine = create_engine(url, echo=debug)

    if setup:
      self.setup()
    else:
      self.session = sessionmaker(self.engine)()

    self.hash_params = self.session.query(Hash).first()

  def setup(self):
    # todo: avoid setting up if tables already exsit and/or have data?
    # as long as we only read the first hash in __init__, we should be
    # ok calling this function again, but it will add extra hash records
    SQLAlchemyBase.metadata.create_all(self.engine)
    self.session = sessionmaker(self.engine)()
    salt = self.random_string()
    rounds = 12345
    hash_params = Hash(salt, rounds)
    self.session.add(hash_params)
    self.session.commit()

  def random_string(self):
    return ''.join(SystemRandom().choice(string.ascii_uppercase + string.digits) for x in range(32))

  def hash(self, email_address):
    # todo: 1. support for other hash algorithms based on hash_params.name
    return sha1_crypt.encrypt(email_address, rounds=self.hash_params.rounds, salt=self.hash_params.salt)

  def find(self, email_address):
    return self.find_hashed(self.hash(email_address))

  def find_hashed(self, hashed_address):
    return self.session.query(BlockedEmail).filter_by(hashed_address=hashed_address).first()

  def add(self, email_address):
    hashed_address = self.hash(email_address)
    if not self.find_hashed(hashed_address):
      block = BlockedEmail(hashed_address)
      self.session.add(block)
      self.session.commit()

def getDatabase(url, setup=False, debug=False):
    db = None
    try:
      db = Database(url, setup, debug)
    except OperationalError as e:
      print "Check that the database exists and DATABASE_URL is configured correctly"
      raise e
    except ProgrammingError as e:
      print "Did you forget to run `./unsubscribe --setup` ?"
      raise e
    return db

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Cryptobot unsubscribe parser")
    parser.add_argument('--setup', dest='setupDB', action='store_true', default=False)
    parser.add_argument('--debug', dest='debugDB', action='store_true', default=False)
    parser.add_argument('--add', dest='email', action='store')
    args = parser.parse_args()

    from config import DATABASE_URL
    db = getDatabase(DATABASE_URL, args.setupDB, args.debugDB)

    if db is None:
      sys.exit(1)

    if args.email:
      if not db.find(args.email):
        db.add(args.email)
      else:
        print "That email is already unsubscribed"

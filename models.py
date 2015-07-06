from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import text
from sqlalchemy.orm import relationship

Base = declarative_base()


class MatchFilters(Base):
    __tablename__ = 'match_filters'
    id = Column(Integer, primary_key=True)
    match_id = Column(Integer, ForeignKey('matches.id'))
    filter_id = Column(Integer, ForeignKey('filters.id'))


class Match(Base):
    __tablename__ = 'matches'
    id = Column(Integer, primary_key=True)
    matches = Column(Text)
    timestamp = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    filters = relationship("Filter",
                           secondary='match_filters')


class Filter(Base):
    __tablename__ = 'filters'
    id = Column(Integer, primary_key=True)
    type = Column(Text)
    args = Column(Text)
    timestamp = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))

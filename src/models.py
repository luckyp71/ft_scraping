from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Article(Base):
    __tablename__ = "articles"
    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String, unique=True)
    title = Column(String)
    text = Column(Text)
    paywalled = Column(Integer, default=0)
    status = Column(String, default="new")

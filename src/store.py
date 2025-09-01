from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.models import Base, Article
import os

DB_PATH = os.getenv("DB_PATH", "data/ft.db")
DATABASE_URL = f"sqlite:///{DB_PATH}"

engine = create_engine(DATABASE_URL, echo=False, future=True)
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False, future=True)


def init_db():
    Base.metadata.create_all(engine)


def save_article(data: dict):
    session = SessionLocal()
    try:
        # Check if URL exists
        existing = session.query(Article).filter_by(url=data["url"]).first()
        if existing:
            return
        article = Article(**data)
        session.add(article)
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"DB save error: {e}")
    finally:
        session.close()

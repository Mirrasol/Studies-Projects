from dotenv import load_dotenv
from sqlalchemy import create_engine  # sync engine
# from sqlalchemy.ext.asyncio import create_async_engine  # async engine
from sqlalchemy.orm import sessionmaker
import os

from project.models import Base

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')
engine = create_engine(DATABASE_URL, echo=False)  # echo печатает в терминале команды, не ставим в проде

session_factory = sessionmaker(bind=engine)
Base.metadata.create_all(engine)

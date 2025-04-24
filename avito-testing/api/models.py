from datetime import datetime
from decimal import Decimal
from sqlalchemy import Integer, String, DateTime, DECIMAL
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from api.app import db


class Base(DeclarativeBase):
    pass


class Advertisement(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    description: Mapped[str] = mapped_column(String(1000), nullable=False)
    price: Mapped[Decimal] = mapped_column(Decimal(precision=10, scale=2), default=Decimal(0.0))
    photos: Mapped[str] = mapped_column(String())
    created_at: Mapped[datetime] = mapped_column(DateTime, default=db.func.now())

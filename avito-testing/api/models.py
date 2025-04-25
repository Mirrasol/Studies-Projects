from datetime import datetime
from decimal import Decimal

from sqlalchemy import DECIMAL, DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from api.db import db


class AdvertisementModel(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    description: Mapped[str] = mapped_column(String(1000), nullable=False)
    price: Mapped[Decimal] = mapped_column(DECIMAL(precision=10, scale=2), default=Decimal(0.0))
    photos: Mapped[str] = mapped_column(String())
    created_at: Mapped[datetime] = mapped_column(DateTime, default=db.func.now())

from flask_sqlalchemy import SQLAlchemy

from api.data import CreateAdvertismentDTO
from api.models import AdvertisementModel


def create_advertisment_service(db: SQLAlchemy, advertisment: CreateAdvertismentDTO):
    created_advertisment = AdvertisementModel(**advertisment.model_dump())
    db.session.add(created_advertisment)
    db.session.commit()
    return dict(
        id=created_advertisment.id,
        name=created_advertisment.name,
        description=created_advertisment.description,
        price=created_advertisment.price,
        photos=created_advertisment.photos,
        created_at=created_advertisment.created_at,
    )

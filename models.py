from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, func
from sqlalchemy.orm import relationship

from database import Base, engine


class IHerbProducts(Base):
    __tablename__ = 'iherb_products'
    id = Column(Integer, primary_key=True, index=True)
    created = Column(DateTime(timezone=True), nullable=False, default=func.now())
    name = Column(String, nullable=False)
    url = Column(String, nullable=False)
    store_id = Column(String, nullable=False)
    category = Column(String, nullable=False)
    images = Column(String, nullable=False)
    brand = Column(String)
    rating = Column(String)
    rating_count = Column(String)
    rating_url = Column(String)
    review_url = Column(String)

    prices = relationship('IHerbPrices', back_populates='products')


class IHerbPrices(Base):
    __tablename__ = 'iherb_prices'
    id = Column(Integer, primary_key=True, index=True)
    created = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    price = Column(String, nullable=False)
    discount = Column(String)
    product_id = Column(Integer, ForeignKey(IHerbProducts.id))

    products = relationship('IHerbProducts', back_populates='prices')


Base.metadata.create_all(engine)

from sqlalchemy import Column, Boolean, String, ARRAY, Integer, DateTime
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Person(Base):
    __tablename__ = "person"

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String(32), nullable=False)
    lastname = Column(String(32), nullable=False)
    spouse_id = Column(Integer, nullable=True)
    kids_ids = Column(ARRAY(Integer))
    is_married = Column(Boolean, nullable=False)

    def __repr__(self):
        return f"id: {self.id}, firstname: {self.firstname}, lastname: {self.lastname}"
        # return 'id: {}, firstname: {}'.format(self.id, self.firstname)


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(32), nullable=False)


class Keys(Base):
    __tablename__ = "keys"
    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, nullable=False)
    created_at = Column(DateTime, default=func.now())
    price = Column(Integer, nullable=False)

    def __repr__(self):
        return f"id={self.id}, code={self.code}, created_at={self.created_at}, price={self.price})"

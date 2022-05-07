from datetime import datetime
from enum import Enum

from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method
from sqlalchemy.ext.associationproxy import association_proxy
from models.dbconn import Base
from sqlalchemy import (
    Column,
    String,
    Integer,
    Text,
    DateTime,
    BigInteger,
    ForeignKey,
    Enum,
    select,
)
from dataclasses import dataclass
from sqlalchemy import func



@dataclass
class Product(Base):
    __tablename__ = "product"
    id: int
    name: str
    category_name: str
    description: str
    buy_price: BigInteger
    sell_price: BigInteger
    quantity: int


    id = Column("id", BigInteger, primary_key=True, autoincrement=True)
    name = Column("name", String(255))
    category_name= Column ("category_name", String(255), nullable=True)
    description= Column ("description", Text, nullable=True)
    buy_price= Column ("buy_price", BigInteger, nullable=True)
    sell_price= Column ("sell_price", BigInteger)
    quantity= Column ("quantity", BigInteger, default = 0)

   
    def __repr__(self):
        return "<Product id={0}, name= {1}>".format(self.id, self.name)


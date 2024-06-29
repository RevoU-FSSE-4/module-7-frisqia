# from models.base import Base
# from sqlalchemy import Integer, String
# from sqlalchemy.orm import mapped_column, relationship


# class Product(Base):
#     __tablename__ = 'products'

#     id = mapped_column(Integer, primary_key=True, autoincrement=True)
#     name = mapped_column(String(30), nullable= False)

#     reviews = relationship("Review", back_populates="product", cascade="all, delete-orphan")
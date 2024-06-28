from models.base import Base
from sqlalchemy import Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import mapped_column
from sqlalchemy.sql import func

class Review(Base):
    __tablename__ = 'reviews'

    id = mapped_column(Integer, primary_key=True)
    username = mapped_column(String, ForeignKey("user.username", ondelete="CASCADE"))
    # product_id = mapped_column(Integer)
    email = mapped_column(String(30), nullable= False)
    rating = mapped_column(Integer)
    review_content = mapped_column(Text)    

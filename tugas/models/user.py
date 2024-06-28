from models.base import Base
from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy import Integer, String
import bcrypt

class Product(Base):
    __tablename__ = 'users'

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    username = mapped_column(String(100), nullable=False)
    email = mapped_column(String(100), nullable=False)
    role = mapped_column(String(100))
    password_hash = mapped_column(String(100), nullable=False)

    #Relationship List

    reviews = relationship("Review", cascade="all,delete-orphan")

    #password yang sudah di encript
    def set_password(self, password):
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    #check
    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))
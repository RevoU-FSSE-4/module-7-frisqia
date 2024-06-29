from models.base import Base
from sqlalchemy.orm import mapped_column
from sqlalchemy import Integer, String

from flask_login import UserMixin

import bcrypt

class User(Base, UserMixin):
    __tablename__ = 'users'

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    username = mapped_column(String(100), nullable=False)
    email = mapped_column(String(100), nullable=False)
    password = mapped_column(String(100), nullable=False)

    # password yang sudah di encript
    def set_password(self, password):
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    # check hashingnya/ membandingkan password yang sudah di input dengan password yang atersimpan
    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))
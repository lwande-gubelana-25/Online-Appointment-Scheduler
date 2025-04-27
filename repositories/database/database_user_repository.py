# repositories/database/database_user_repository.py

from repositories.repository import Repository
from src.user import User
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String

# Define the SQLAlchemy base
Base = declarative_base()

# Define the User model for the database
class UserModel(Base):
    __tablename__ = 'users'
    id = Column(String, primary_key=True)
    name = Column(String)
    email = Column(String)
    phone = Column(String)
    password = Column(String)
    role = Column(String)

class DatabaseUserRepository(Repository):
    def __init__(self, db_url: str):
        # Create a database engine and session factory
        self.engine = create_engine(db_url)
        self.Session = sessionmaker(bind=self.engine)

        # Create tables in the database (if they don't exist)
        Base.metadata.create_all(self.engine)

    def save(self, user: User) -> None:
        session = self.Session()
        user_model = UserModel(
            id=user.id,
            name=user.name,
            email=user.email,
            phone=user.phone,
            password=user.password,
            role=user.role
        )
        session.add(user_model)
        session.commit()
        session.close()

    def find_by_id(self, id: str):
        session = self.Session()
        user_model = session.query(UserModel).filter_by(id=id).first()
        session.close()
        return user_model

    def find_all(self):
        session = self.Session()
        users = session.query(UserModel).all()
        session.close()
        return users

    def delete(self, id: str) -> None:
        session = self.Session()
        user_model = session.query(UserModel).filter_by(id=id).first()
        if user_model:
            session.delete(user_model)
            session.commit()
        session.close()

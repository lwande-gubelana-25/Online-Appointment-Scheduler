from repositories.inmemory.in_memory_user_repository import InMemoryUserRepository
from src.user import User

user_repo = InMemoryUserRepository()

def create_user(user: User):
    user_repo.save(user)

def get_user(user_id: str):
    return user_repo.find_by_id(user_id)

def get_all_users():
    return user_repo.find_all()

def delete_user(user_id: str):
    user_repo.delete(user_id)

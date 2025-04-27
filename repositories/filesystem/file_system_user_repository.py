# repositories/filesystem/file_system_user_repository.py

import json
from repositories.repository import Repository
from src.user import User

class FileSystemUserRepository(Repository):
    def __init__(self, file_path: str):
        self._file_path = file_path

    def save(self, user: User) -> None:
        users = self._load_all()
        users[user.id] = user.__dict__  # Assuming the User object is serializable to a dictionary
        with open(self._file_path, 'w') as f:
            json.dump(users, f)

    def find_by_id(self, id: str):
        users = self._load_all()
        return users.get(id)

    def find_all(self):
        return list(self._load_all().values())

    def delete(self, id: str) -> None:
        users = self._load_all()
        if id in users:
            del users[id]
            with open(self._file_path, 'w') as f:
                json.dump(users, f)

    def _load_all(self):
        try:
            with open(self._file_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}  # Return an empty dictionary if the file doesn't exist

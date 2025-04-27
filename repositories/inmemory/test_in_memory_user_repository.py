import unittest
from repositories.inmemory.in_memory_user_repository import InMemoryUserRepository
from src.user import User

class TestInMemoryUserRepository(unittest.TestCase):

    def setUp(self):
        self.repo = InMemoryUserRepository()

    def test_save_and_find(self):
        user = User("U1", "Alice", "alice@example.com", "1234567890", "password", "patient")
        self.repo.save(user)
        result = self.repo.find_by_id("U1")
        self.assertIsNotNone(result)
        self.assertEqual(result.name, "Alice")

    def test_find_all(self):
        user1 = User("U2", "Bob", "bob@example.com", "1234567890", "password", "doctor")
        user2 = User("U3", "Charlie", "charlie@example.com", "1234567890", "password", "patient")
        self.repo.save(user1)
        self.repo.save(user2)
        results = self.repo.find_all()
        self.assertEqual(len(results), 2)

    def test_delete(self):
        user = User("U4", "Diana", "diana@example.com", "1234567890", "password", "admin")
        self.repo.save(user)
        self.repo.delete("U4")
        self.assertIsNone(self.repo.find_by_id("U4"))

if __name__ == "__main__":
    unittest.main()

from repositories.repository import Repository
from src.service import Service

class ServiceRepository(Repository[Service, str]):
    pass
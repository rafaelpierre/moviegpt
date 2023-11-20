from pydantic import BaseModel, computed_field
import chromadb
from chromadb.config import Settings

class ChromaHelper(BaseModel):

    path: str = "db/"

    @computed_field()
    @property
    def client(self) -> chromadb.Client:

        client = chromadb.PersistentClient(path = self.path)
        return client
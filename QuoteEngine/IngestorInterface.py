"""Strategy object abstract class for a collection of ingestors."""

from abc import ABC, abstractmethod
from typing import List

from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """Base class for a collection of ingestors."""

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Decides if a file can be ingested."""
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(self, path: str) -> List[QuoteModel]:
        """Abstract method to take in files and convert quotes."""
        pass

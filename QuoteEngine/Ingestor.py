"""Select a suitable ingestor for a file which needs to be ingested."""

from typing import List

from .IngestorInterface import IngestorInterface
from .DOCXIngestor import DOCXIngestor
from .CSVIngestor import CSVIngestor
from .PDFIngestor import PDFIngestor
from .TXTIngestor import TXTIngestor


class Ingestor(IngestorInterface):
    """Take file path, select suitable ingestor, return list of quotes."""

    ingestors = [CSVIngestor, DOCXIngestor, PDFIngestor, TXTIngestor]

    @classmethod
    def parse(cls, path):
        """Iterate through ingestors, select if suitable one can be found."""
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)

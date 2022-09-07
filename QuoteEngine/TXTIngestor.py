"""A TXT Ingestor to parse quotes from a TXT file.

Takes a file path and returns a list of quotes containing QuoteModel of
quote body and author if the file can be parsed.
"""

from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TXTIngestor(IngestorInterface):
    """TXT Ingestor strategy object.

    Inherits from IngestorInterface class. Tests if file extension can
    be parsed and raises an exception if it cannot. Creates a random
    text file to copy text to. Splits the lines to generate a quote body
    and author required for QuoteModel class. Returns list of QuoteModels.
    """

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Take the path of a file and tests if this can be ingested."""
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest exception')

        quotes = []
        with open(path) as f:
            lines = f.readlines()
            for line in lines:
                if len(line) > 0:
                    parse = line.split(' - ')
                    new_quote = QuoteModel(parse[0], parse[1])
                    quotes.append(new_quote)

        return quotes

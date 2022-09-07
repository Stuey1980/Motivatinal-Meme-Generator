"""A PDF Ingestor to parse quotes from a PDF file.

Takes a file path and returns a list of quotes containing QuoteModel of
quote body and author if the file can be parsed.
"""

from typing import List
import subprocess
import os
import random

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    """PDF Ingestor strategy object.

    Inherits from IngestorInterface class. Tests if file extension can be
    parsed and raises an exception if it cannot. Creates a random text file
    to copy text to. Splits the lines to generate a quote body and author
    required for QuoteModel class. Returns list of QuoteModels.
    """

    allowed_extensions = ['pdf']

    def parse(self, path: str) -> List[QuoteModel]:
        """Take the path of a file and tests if this can be ingested."""
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest exeption')

        tmp = f'./tmp/{random.randint(0, 100000000)}.txt'

        call = subprocess.call(['pdftotext', path, tmp])

        file_ref = open(tmp, "r")
        quotes = []

        for line in file_ref.readlines():
            line = line.strip('/n/r').strip()
            if len(line) > 0:
                parse = line.split(',')
                new_quote = QuoteModel(parse[0], parse[1])
                quotes.append(new_quote)

        file_ref.close()
        os.remove(tmp)

        return quotes

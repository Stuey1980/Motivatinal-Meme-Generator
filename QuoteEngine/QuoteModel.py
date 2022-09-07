"""Quote model class."""


class QuoteModel():
    """The class for a quote model."""

    def __init__(self, quote: str, author: str):
        """Initialise quote model containing quote body and author."""
        self.quote = quote
        self.author = author

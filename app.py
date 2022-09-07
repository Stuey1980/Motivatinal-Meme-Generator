import random
import os
import requests
import urllib.request
from flask import Flask, render_template, abort, request

# Import your Ingestor and MemeEngine classes
from QuoteEngine import IngestorInterface
from QuoteEngine import Ingestor
from QuoteEngine import CSVIngestor
from QuoteEngine import DOCXIngestor
from QuoteEngine import PDFIngestor
from QuoteEngine import TXTIngestor
from QuoteEngine import QuoteModel
from MemeEngine import MemeEngine


app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    # Use the Ingestor class to parse all files in the
    # quote_files variable
    quotes = []

    for file in quote_files:
        quotes.append(Ingestor.parse(file))

    images_path = "./_data/photos/dog/"

    imgs = [file for file in images_path]

    # Use the pythons standard library os class to find all
    # images within the images images_path directory

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    # Use the random python standard library class to:
    # 1. select a random image from imgs array
    # 2. select a random quote from the quotes array

    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    # 1. Use requests to save the image from the image_url
    #    form param to a temp local file.
    # 2. Use the meme object to generate a meme using this temp
    #    file and the body and author form paramaters.
    # 3. Remove the temporary saved image.

    image_url = request.form.get('image_url')
    body = request.form.get('body')
    author = request.form.get('author')
    tmp = f'{random.randint(0, 1000000)}.png'
    urllib.request.urlretrieve(image_url, tmp)
    path = make_meme(tmp, body, author)
    os.remove(tmp)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
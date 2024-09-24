
import json
# Python's built-in module for opening and reading URLs
from urllib.request import urlopen

# sample ISBN for testing: 1593276036
def isbnsearch1(isbnno):
    api = "https://www.googleapis.com/books/v1/volumes?q=isbn:"

    # send a request and get a JSON response
    resp = urlopen(api + isbnno)
    # parse JSON into Python as a dictionary
    book_data = json.load(resp)

    # create additional variables for easy querying
    volume_info = book_data["items"][0]["volumeInfo"]
    book_data3=[volume_info['title'],volume_info['authors'][0],volume_info['publisher'],volume_info['categories'][0]]

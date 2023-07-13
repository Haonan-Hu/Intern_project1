from pytrends.request import TrendReq
from pytrends.exceptions import ResponseError
from src.YAKE import rertive_keywords
import pdfkit

def Interest_over_time(url):
    # Make your request to the Google API
    pytrends = TrendReq(hl='en-US', tz=360)
    keywords = rertive_keywords(url)
    pytrends.build_payload(keywords, cat=0, timeframe='today 5-y', geo='', gprop='')
    # extract interest over time data and handle exceptions by making too many requests at a time
    while True:
        try:
            response = pytrends.interest_over_time()
            break
        except ResponseError:
            print("Making too many requests, please try again later.")
    # attempt to request data until successful

    # Convert DataFrame to HTML table
    html_table = response.to_html()
    # Convert HTML table to PDF
    pdfkit.from_string(html_table, 'interest_over_time.pdf')


def trends():
    # Get the URL from the user
    url = input("Please enter the URL: ")
    # Make the request for interest over time data
    Interest_over_time(url)


if __name__ == '__main__':
    trends()

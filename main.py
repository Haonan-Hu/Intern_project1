from pytrends.request import TrendReq
from src.YAKE import rertive_keywords
from tabulate import tabulate
from IPython.display import display
import pandas as pd
import time
import numpy as np
import pdfkit

def make_request(url):
    # Make your request to the Google API
    pytrends = TrendReq(hl='en-US', tz=360)
    keywords = rertive_keywords(url)
    pytrends.build_payload(keywords, cat=0, timeframe='today 5-y', geo='', gprop='')
    # attempt to request data until successful
    response = pytrends.interest_over_time()
    if response is None:
        # Sleep for the amount of seconds specified in the Retry-After header
        retry_after = int(response.headers.get('Retry-After'))
        time.sleep(retry_after)
        # Retry the request
        return make_request()
    # Handle other response statuses here
    else:
        # Process the response
        return response


def trends():
    # Get the URL from the user
    url = input("Please enter the URL: ")
    # Make the request
    trends_data = make_request(url)
    # print(tabulate(trends_data, headers='keys', tablefmt='psql'))

    return trends_data


if __name__ == '__main__':
    result = trends()
    # Convert DataFrame to HTML table
    html_table = result.to_html()
    # Convert HTML table to PDF
    pdfkit.from_string(html_table, 'output.pdf')

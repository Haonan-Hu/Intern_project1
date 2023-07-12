from pytrends.request import TrendReq
from YAKE import rertive_keywords
import pandas as pd
import time
from tabulate import tabulate
from IPython.display import display


def trends():
    pytrends = TrendReq(hl='en-US', tz=360)

    keywords = rertive_keywords()
    pytrends.build_payload(keywords, cat=0, timeframe='today 5-y', geo='', gprop='')
    for i in range(3):
        # Send the request
        trends_data = pytrends.interest_over_time()
        # Add a delay between requests
        time.sleep(1)

    # print(tabulate(trends_data, headers='keys', tablefmt='psql'))

    # Apply styling to the DataFrame
    df1 = trends_data.style.set_table_styles([dict(selector='th', props=[('text-align', 'center')])])
    df2 = df1.set_properties(**{'text-align': 'center'})
    return df2


if __name__ == '__main__':
    result = trends()
    # Render and display the styled DataFrame directly
    display(result)

import requests
from bs4 import BeautifulSoup


def scrape_url(url):
    url = input("Please enter the URL: ")
    # Send a GET request to the URL
    response = requests.get(url)

    # Get the content of the response
    content = response.text

    # Create a BeautifulSoup object to parse the HTML
    soup = BeautifulSoup(content, 'html.parser')

    return soup.get_text()


if __name__ == '__main__':
    url = ''
    print(scrape_url(url))

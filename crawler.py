import requests
from bs4 import BeautifulSoup

# Function to crawl a website
def crawl_website(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find and extract relevant information from the page
        # For example, extract all links from the page
        links = soup.find_all('a')

        # Print the extracted links
        for link in links:
            print(link.get('href'))

    else:
        print("Failed to retrieve webpage. Status code:", response.status_code)

# Example usage
crawl_website('http://example.com')

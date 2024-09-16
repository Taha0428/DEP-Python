import requests
from bs4 import BeautifulSoup
import csv

url = 'http://quotes.toscrape.com/'
page = 1

# Open CSV file to write the data
with open('quotes_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Quote", "Author", "Tags"])

    while True:
        # Request the page
        try:
            response = requests.get(url + f'page/{page}/')
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching page {page}: {e}")
            break

        soup = BeautifulSoup(response.content, 'html.parser')

        # Get all quotes on the page
        quotes = soup.find_all('div', class_='quote')
        if not quotes:
            print(f"No more quotes found. Scraping completed at page {page}.")
            break

        # Extract and write quote data to CSV
        for quote in quotes:
            text = quote.find('span', class_='text').text
            author = quote.find('small', class_='author').text
            tags = [tag.text for tag in quote.find_all('a', class_='tag')]

            writer.writerow([text, author, ', '.join(tags)])

        print(f"Page {page} scraped successfully.")
        page += 1

print("All pages scraped! Data has been saved to quotes_data.csv.")
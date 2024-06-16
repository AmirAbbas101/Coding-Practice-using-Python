import requests
from bs4 import BeautifulSoup

# Send a GET request to the website
url = 'https://learndjango.com/tutorials/'
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Create a BeautifulSoup object and parse the HTML
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all the article titles
    tutorials = soup.find_all('li', class_='tutorials')
    
    # Print the titles
    for tutorial in tutorials:
        title = tutorial.find('h3')
        if title:
            print(title.text.strip())
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

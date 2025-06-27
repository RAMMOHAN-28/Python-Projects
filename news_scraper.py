import requests
from bs4 import BeautifulSoup

URL = "https://www.bbc.com/news"

response = requests.get(URL)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find_all(['h3', 'h2'], limit=20)

    titles = [headline.get_text(strip=True) for headline in headlines if headline.get_text(strip=True)]

    with open("headlines.txt", "w", encoding='utf-8') as file:
        for idx, title in enumerate(titles, start=1):
            file.write(f"{idx}. {title}\n")

    print("✅ Headlines successfully saved to 'headlines.txt'")
else:
    print(f"❌ Failed to retrieve page. Status code: {response.status_code}")

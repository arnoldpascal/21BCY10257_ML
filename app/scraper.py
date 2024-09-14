import requests
from bs4 import BeautifulSoup
from .models import Document, SessionLocal

def scrape_news():
    session = SessionLocal()
    url = "https://news.ycombinator.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    articles = soup.find_all("a", class_="storylink")

    for article in articles:
        new_doc = Document(text=article.get_text())
        session.add(new_doc)
    
    session.commit()

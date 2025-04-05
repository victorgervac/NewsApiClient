from newsapi import NewsApiClient
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Access your API key
api_key = os.getenv("NEWS_API_KEY")

newsapi = NewsApiClient(api_key=api_key)

news = newsapi.get_top_headlines(category="business", language="en")

for article in news["articles"]:
    print(article["title"])

from src.seed_urls import get_ft_seed_urls
from src.parse import fetch_article
from src.store import save_article


async def crawl():
    article_urls = get_ft_seed_urls()
    for url in article_urls:
        article_data = fetch_article(url)
        if article_data and article_data["text"]:
            save_article(article_data)
        else:
            print(f"No text found at {url}")

import requests
from bs4 import BeautifulSoup


def extract_text(html):
    soup = BeautifulSoup(html, "html.parser")
    article_text = []

    # Try main content
    for p in soup.find_all("p"):
        article_text.append(p.get_text(strip=True))

    text = "\n".join(article_text).strip()
    return {"title": "", "text": text, "paywalled": 0, "status": "new"}


def fetch_article(url):
    try:
        resp = requests.get(url, timeout=10)
        if resp.status_code == 200:
            data = extract_text(resp.text)
            data["url"] = url
            return data
    except Exception as e:
        print(f"Failed to fetch {url}: {e}")
    return None

import feedparser

RSS_FEEDS = [
    "https://www.ft.com/world?format=rss",
    "https://www.ft.com/technology?format=rss",
    "https://www.ft.com/economy?format=rss"
]


def get_ft_seed_urls():
    urls = []
    for feed in RSS_FEEDS:
        parsed = feedparser.parse(feed)
        urls.extend([entry.link for entry in parsed.entries])
    return urls

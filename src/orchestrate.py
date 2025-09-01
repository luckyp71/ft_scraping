from src.store import init_db
from src.crawl import crawl
from src.theming import analyze_themes
from src.make_ppt import generate_presentation
import asyncio


def run_pipeline():
    print("pipeline start")
    init_db()
    asyncio.run(crawl())
    themes = analyze_themes()
    if themes:
        generate_presentation(themes)
    else:
        print("No themes to generate PPT")
    print("pipeline stop")


if __name__ == "__main__":
    run_pipeline()

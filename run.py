import json

from app.src import PagesScrapper

PAGES = ["kwejk", "JBZD"]
N_PAGES = 25


def main():
    pages_scrapper = PagesScrapper()

    memes = pages_scrapper.scrap_pages(PAGES, N_PAGES)

    with open("memes.json", "w") as file:
        json.dump(memes, file)


if __name__ == "__main__":
    main()

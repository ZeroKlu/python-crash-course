from urllib.request import urlopen
from bs4 import BeautifulSoup

def scrape_with_soup(url: str) -> BeautifulSoup:
    """Returns soup object"""
    page = urlopen(url)
    html = page.read().decode("utf-8")
    return BeautifulSoup(html, "html.parser")

def main() -> None:
    url = "http://olympus.realpython.org/profiles"
    soup = scrape_with_soup(url)
    print(soup.prettify())

if __name__ == "__main__":
    main()

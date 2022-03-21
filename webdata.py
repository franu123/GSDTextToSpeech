import requests
from bs4 import BeautifulSoup


class GSDWebScrapper():
    URL = None
    html_id = None

    def __init__(self):
        print("Object Initialised")

    def html_content(self):
        page = requests.get(self.URL)

        soup = BeautifulSoup(page.content, "html.parser")

        results = soup.find(id=self.html_id)

        required_data = results.prettify()

        return required_data

    def display_data(self):
        data = self.html_content()
        return data


def get_data_from_web():
    gsd_url = "https://www.moneycontrol.com/"
    gsd_id = "maNSE"
    gsd_scraper = GSDWebScrapper()
    gsd_scraper.URL = gsd_url
    gsd_scraper.html_id = gsd_id
    data = gsd_scraper.display_data()
    return data

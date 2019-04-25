import re

from bs4 import BeautifulSoup
from urllib.parse import urlparse


class HtmlParser(object):

    def parse(self, page_url, html_content):

        if page_url is None or html_content is None:
            return None
        soup = BeautifulSoup(html_content, "html.parser", from_encoding="utf-8")
        new_urls = self.get_new_urls(page_url, soup)
        new_data = self.get_new_data(page_url, soup)

    def get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r"/view/\d+\.htm"))
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.join(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def get_new_data(self, page_url, soup):
        res_data = {}

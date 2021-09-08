from bs4 import BeautifulSoup
import requests

class WebScraper:
    def __init__(self, url):
        self.url = url
        self.req = requests.get(self.url, headers={'User-Agent': 'Mozilla/5.0'})
        self.soup = BeautifulSoup(self.req.text, 'html.parser')
        self.hrefs = []

    def crawling(self, soup):
        div = soup.find("div", class_="_article_body_contents")
        div2 = soup.find("h3", id="articleTitle")
        result = div.get_text()
        title = div2.get_text()
        return result, title

    def get_href(self):
        result = []
        div = self.soup.find("div", class_="main_content_inner _content_inner")

        for anchor in div.find_all("li"):
            href = anchor.find("a")["href"]
            if (href[0]=="/"):
                result.append("https://news.naver.com"+href)
                self.hrefs.append("https://news.naver.com"+href)
            else:
                result.append(href)
                self.hrefs.append(href)

        return result

    def main(self):
        list_href = self.get_href()
        contents = []
        titles = []

        for href in list_href:
            href_req = requests.get(href, headers={'User-Agent': 'Mozilla/5.0'})
            href_soup = BeautifulSoup(href_req.text, "html.parser")
            content, title = self.crawling(href_soup)
            contents.append(content)
            titles.append(title)

        return titles, contents, self.hrefs

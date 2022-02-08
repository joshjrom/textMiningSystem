from bs4 import BeautifulSoup
import requests

def getPageData(pageUrl):
    res = requests.get(pageUrl)
    soup = BeautifulSoup(res.text, "html.parser")


    nameOfArticle = str(soup.find_all("h1", {"class": "heading-title"})[0].string).strip()
    abstractOfArticle = str(soup.find_all("div", {"class": "abstract-content"})[0].p.string).strip()

    return {
        "nameOfArticle": nameOfArticle,
        "abstractOfArticle": abstractOfArticle
    }



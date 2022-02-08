from bs4 import BeautifulSoup
import requests


def getPageData(pageUrl):
    res = requests.get(pageUrl)
    soup = BeautifulSoup(res.text, "html.parser")
    
    # titleOfArticle = soup.find_all("div", {"class": "highwire-cite-title"})
    # abstractOfArticle = soup.find_all("p", {"id": "p-1"})


    articleTitleDiv = soup.find("div", class_="highwire-cite-title")
    articleTitle = articleTitleDiv.text
    

    articleAbstractDiv = soup.find("p", id="p-1")
    articleAbstract = articleAbstractDiv.text

    return {
        "nameOfArticle": articleTitle,
        "abstractOfArticle": articleAbstract
    }
   


print(getPageData("https://adc.bmj.com/content/94/9/713"))

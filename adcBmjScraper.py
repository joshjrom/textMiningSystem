from bs4 import BeautifulSoup
import requests
from adcBmjArticleScraper import getPageData

#root url of https://adc.bmj.com/
rootUrl = "https://adc.bmj.com"

#page number from search box on pubmed. "sicklecell Nigeria" was searched to provide search pages
pageToScrape = 2

# using requests library to read the url and creating a Beautifulsoup object
res = requests.get(f"{rootUrl}/search/sickle%252Bcell%252BNigeria%20jcode%3Aarchdischild?page={pageToScrape}")
soup = BeautifulSoup(res.text, "html.parser")

# using find_all method on the soup object to get all "a" tags with class docsum-title holding href link e.g. href="/content/50/12/948"
articleLinkTags = soup.find_all("a", {"class": "highwire-cite-linked-title"})


# looping through all href article title links on the the search page and appending them to articleIds variable
def getArticleIds(arrayOfAnchorTags):
    articleIds = []
    for item in arrayOfAnchorTags:
        articleIds.append(item.get("href"))
        
    return articleIds

allArticleIds = getArticleIds(articleLinkTags)


# looping through all href link and appending rooturl and href e.g. "https://adc.bmj.com" + /content/50/12/948
def getAllPageLinks(arrayOfArticleIds):
    pageLinks = []
    for item in arrayOfArticleIds:
        pageLinks.append(f"{rootUrl}{item}")
        
    
    return pageLinks

articleLinks = getAllPageLinks(allArticleIds)


# looping through the full links and requesting for title and abstract using the getPageData function and appending each to finalOutput variable
finalOutput = []

for url in articleLinks:
    try:
        finalOutput.append(getPageData(url))
    except:
        pass


print(finalOutput)


from bs4 import BeautifulSoup 
import requests
from pubMedArticlePageScraper import getPageData
from pandas import DataFrame, ExcelWriter

# root url of pubmed.com
rootUrl = "https://pubmed.ncbi.nlm.nih.gov"

# page number from search box on pubmed. "sicklecell Nigeria" was searched to provide search pages
pagetoScrape = 1

# using requests library to read the url and creating a Beautifulsoup object
res = requests.get(f"{rootUrl}/?term=SickleCell%20Nigeria&page={pagetoScrape}")
soup = BeautifulSoup(res.text, "html.parser")

# using find_all method on the soup object to get all "a" tags with class docsum-title holding href link e.g. href="/34795735/"
articleLinkTags = soup.find_all("a", {"class": "docsum-title"})

# looping through all href article title links on the the search page and appending them to articleIds variable
def getArticleIds(arrayOfAnchorTags):
    articleIds = []
    for item in arrayOfAnchorTags:
        articleIds.append(item.get("href"))

    return articleIds

allArticleIds = getArticleIds(articleLinkTags)


# looping through all href link and appending rooturl and href e.g. "https://pubmed.ncbi.nlm.nih.gov" + "/34795735/"
def getPageLinks(arrayOfArticleIds):
    pageLinks = []

    for item in arrayOfArticleIds: 
        pageLinks.append(f"{rootUrl}{item}")

    return pageLinks

articleLinks  = getPageLinks(allArticleIds)


# looping through the full links and requesting for title and abstract using the getPageData function and appending each to finalOutput variable
finalOutput = []

for url in articleLinks:
    try:
        finalOutput.append(getPageData(url))
    except:
        pass


print(finalOutput)


# using pandas library to create a table
# table = DataFrame({
#     "NAME OF ARTICLE": [item.get("nameOfArticle") for item in finalOutput],
#     "ABSTRACT OF ARTICLE": [item.get("abstractOfArticle") for item in finalOutput],
# })


# using csv method to create csv file containing the name and abstract of articles
# table.to_csv("output.csv")


# excel_table = ExcelWriter("output.xlsx", engine="xlsxwriter")

# table.to_excel(excel_table, sheet_name=f"Sheet{pagetoScrape}")


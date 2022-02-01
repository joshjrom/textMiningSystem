from bs4 import BeautifulSoup 
import requests
from articlePageScraper import getPageData
from pandas import DataFrame, ExcelWriter

rootUrl = "https://pubmed.ncbi.nlm.nih.gov"
pagetoScrape = 1

res = requests.get(f"{rootUrl}/?term=SickleCell%20Nigeria&page={pagetoScrape}")
soup = BeautifulSoup(res.text, "html.parser")

articleLinkTags = soup.find_all("a", {"class": "docsum-title"})

def getArticleIds(arrayOfAnchorTags):
    articleIds = []
    for item in arrayOfAnchorTags:
        articleIds.append(item.get("href"))

    return articleIds

allArticleIds = getArticleIds(articleLinkTags)

def getPageLinks(arrayOfArticleIds):
    pageLinks = []

    for item in arrayOfArticleIds: 
        pageLinks.append(f"{rootUrl}{item}")

    return pageLinks


articleLinks  = getPageLinks(allArticleIds)

finalOutput = []

for url in articleLinks:
    try:
        finalOutput.append(getPageData(url))
    except:
        pass


print(finalOutput)


# table = DataFrame({
#     "NAME OF ARTICLE": [item.get("nameOfArticle") for item in finalOutput],
#     "ABSTRACT OF ARTICLE": [item.get("abstractOfArticle") for item in finalOutput],
# })

# excel_table = ExcelWriter("output.xlsx", engine="xlsxwriter")

# table.to_excel(excel_table, sheet_name=f"Sheet{pagetoScrape}")


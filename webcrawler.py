from bs4 import BeautifulSoup
import requests



pubMedResponse = requests.get("https://pubmed.ncbi.nlm.nih.gov/?term=sicklecell+nigeria")

print(pubMedResponse.text)
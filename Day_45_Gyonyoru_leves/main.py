from bs4 import BeautifulSoup
import requests

# with open("website.html") as data_file:
#     contents = data_file.read()
#
# # print(contents)
#
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.prettify())
#
# #soup.find_all(keresesi_kriteriak) --> megtalalja az osszeset
#
# #soup.find(keresesi_kriteriak) --> az elsot talalja meg
#
# #
#
#
# all_anchor_tags = soup.find_all(name="a")
# # for tag in all_anchor_tags:
# #     print(tag.get("href"))
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.get("class"))
# print(section_heading.getText())
# print(section_heading.name)
#
# company_url = soup.select_one(selector="p a")
# print(company_url.get("href"))
#
# name = soup.select_one(selector="#name")
# print(name.getText())
#
# heading_class = soup.select(selector=".heading")
# print(heading_class[0].getText())

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

article_texts = []
article_links = []


articles = soup.find_all(name="a", class_="storylink")
for article in articles:
    article_text = article.getText()
    article_link = article.get("href")
    article_texts.append(article_text)
    article_links.append(article_link)


article_scores = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# print(article_texts)
# print(article_links)
# print(article_scores)


idx = article_scores.index(max(article_scores))
print(article_texts[idx] + "\n" + article_links[idx])


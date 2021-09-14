import bs4
import requests

url = "https://www.passiton.com/inspirational-quotes?pages=2"

response = requests.get(url)

# html parser or beautiful sout only need the content
soup = bs4.BeautifulSoup(response.content, features="html5lib")
# print(soup)

# soup object is a html
# #find all article tag
article_elem = soup.findAll('img')
article = article_elem[0]
print(article)

image = article.attrs['src']
# image is binary format so write as wb binary
with open('abc.jpg', 'wb') as file:
    img_url = article.attrs['src']
    res = requests.get(img_url)
    file.write(res.content)

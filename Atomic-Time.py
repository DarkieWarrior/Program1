import urllib
urllib.request urllib.request.urlopen(https://time.is)

from bs4 import BeautifulSoup
soup = BeautifulSoup(https://time.is , 'html.parser')

print(soup.prettify())

list(soup.children)
[type(< DIV
id="clock0_bg" >) for item in list(soup.children)]
html = list(soup.children)[2]
list(html.children)
body = list(html.children)[3]
list(body.children)
p = list(body.children)[1]

import urllib.request
import bs4

url = "https://www.nate.com"
res = urllib.request.urlopen(url)
webpage = res.read()
bs0bject = bs4.BeautifulSoup(webpage,'html.parser')

tag = bs0bject.find('div', {'id','NateBi'})
print(tag, '\n')

a_tag = tag.find("a")
print(a_tag, '\n')

href = a_tag['href']
print(href, '\n')

text = a_tag.text
print(text)

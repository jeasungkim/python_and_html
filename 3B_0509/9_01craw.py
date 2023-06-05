import urllib.request
import bs4

url = "https://www.nate.com"
res = urllib.request.urlopen(url)
#html - res.read()

bsobject = bs4.BeautifulSoup(res,'html.parser')
tag_div = bsobject.find('div')
#print(bsobject)
print(tag_div)

tag_id = tag_div.find('news_area')
print(tag_id)
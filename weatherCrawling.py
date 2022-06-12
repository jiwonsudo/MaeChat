import urllib3
import bs4

location = '대구'
enc_location = urllib3.parse.quote(location + '+날씨')

url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query='+ enc_location

req = Request(url)
page = urlopen(req)
html = page.read()
soup = bs4.BeautifulSoup(html,'html5lib')
print('오늘 ' + location + '온도는 ' + soup.find('div', class_='temperature_text').text + '도 입니다. ' + '날씨는 ' + soup.find('span', class_= 'weather before_slash').text + ' 입니다.')
from urllib.request import urlopen
from bs4 import BeautifulSoup

#bytes / binary

#1. Dowload html content
website = urlopen ('http://dantri.com.vn')
html_content  = website.read().decode('utf8')
website.close()

#2. Create BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')
ul_news = soup.find('ul', 'ul1 ulnew')
li_new_list = ul_news.find_all('li')

for li in li_new_list:
    a_detail = li.h4.a
    title = a_detail['title'] #attribute
    content = a_detail.string #content / string / value
    print (a_detail)
    print ("-" * 20)

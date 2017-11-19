from urllib.request import urlopen
from bs4 import BeautifulSoup

website = urlopen ('http://nhaczingmp3.com/bang-xep-hang/bai-hat-Viet-Nam/IWZ9Z08I.html')
html_content = website.read().decode("utf8")
website.close()

soup = BeautifulSoup(html_content, 'html.parser')
ul_box_song = soup.find('ul', 'box-song' )
li_new_list = ul_box_song.find_all('li')

for li in li_new_list:
    a_detail = li.div.h3.a
    print (a_detail.get_text())

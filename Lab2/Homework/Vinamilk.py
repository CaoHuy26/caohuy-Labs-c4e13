from urllib.request import urlopen
from bs4 import BeautifulSoup

website = urlopen ('http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn')
html_content = website.read().decode('utf8')
website.close()

soup = BeautifulSoup (html_content, 'html.parser')
table_content = soup.find (id = 'tableContent')
td_new_list = table_content.find_all ("td")

for td in td_new_list:
    print (td.get_text())

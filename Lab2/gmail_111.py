from gmail import *
from random import choice

f_names = ['1.html', '2.html', '3.html']
f_name = choice (f_names)

reasons = ['ebola', 'hiv', 'sida']
reason = choice (reasons)

f = open(f_name)
html_content = f.read()
f.close()

html_content = html_content.replace('{{reason}}', reason)


gmail = GMail('huy.clone2610@gmail.com', 'huy26101997')
msg = Message ("Text Message", to = 'huy.clone2610@gmail.com', html = html_content)
gmail.send(msg)

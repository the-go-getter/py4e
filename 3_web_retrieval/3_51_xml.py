import xml.etree.ElementTree as ET
from urllib.request import urlopen

url = "http://py4e-data.dr-chuck.net/comments_746566.xml"
xml = urlopen(url).read()
# data = '''
# <person>
#     <name>Chuck</name>
#     <phone type="intl">
#         +1 734 303 4456
#     </phone>
#     <email hide="yes" />
# </person>'''
tree = ET.fromstring(xml)
counts = tree.findall('.//count')
# print('Name:', tree.find('name').text)
# print('Attr:', tree.find('email').get('hide'))
sum = 0
for count in counts:
    sum = sum + int(count.text)

print(sum)
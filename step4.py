import requests

responce = requests.get('https://kpk.kss45.ru/%D1%83%D1%87%D0%B5%D0%B1%D0%BD%D0%B0%D1%8F-'
                        '%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0/%D1%80%D0%B0%D1%81%D0%BF%D0%B8%D1%'
                        '81%D0%B0%D0%BD%D0%B8%D0%B5_%D0%BF%D0%B0%D1%80.html')

print(responce)
print(type(responce))
print(dir(responce))
content = responce.content.decode('utf-8')
hrefs = content.split('href=')
# print(hrefs[0])
href_1 = hrefs[1].split('/>')[0]
print(href_1)
print('.xls' in href_1)

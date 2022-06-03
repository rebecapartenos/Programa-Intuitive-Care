import urllib.request
import requests as req
from bs4 import BeautifulSoup
import zipfile

gov = 'https://www.gov.br/ans/pt-br/assuntos/consumidor/o-que-o-seu-plano-de-saude-deve-cobrir-1/o-que-e-o-rol-de-procedimentos-e-evento-em-saude'
page = urllib.request.urlopen(gov)
soup = BeautifulSoup(page, 'html5lib')
list_item = soup.select('p.callout a[href*="Anexo"]')
z = zipfile.ZipFile('Arquivo.zip', 'w', zipfile.ZIP_DEFLATED)
for i, item in  enumerate(list_item, start=0):
    URL = (item.attrs['href'])
    file = req.get(URL, allow_redirects=True)
    link=(file.url.split('/'))
    open(link[-1], 'wb').write(file.content)
    z.write(link[-1])
z.close()

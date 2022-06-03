from urllib import request
import tabula
import pandas
import zipfile

file_url = 'https://www.gov.br/ans/pt-br/arquivos/assuntos/consumidor/o-que-seu-plano-deve-cobrir/Anexo_I_Rol_2021RN_465.2021_RN473_RN478_RN480_RN513_RN536.pdf'
file = 'anexoI.pdf'

request.urlretrieve(file_url, file)
tabula.convert_into("anexoI.pdf", "output.csv", output_format="csv", pages='all')
z = zipfile.ZipFile('Arquivo.zip', 'w', zipfile.ZIP_DEFLATED)
z.write("output.csv")
z.close()
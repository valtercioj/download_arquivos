import sys 
import os

plat = sys.platform
if plat == 'win32':
	try:
		import requests
	except:
		os.system('pip install requests')
		import requests
elif plat == 'linux':
	try:
		import requests
	except:
		os.system('pip3 install requests')
		import requests


def baixar_arquivo(url, endereco=None):
    if endereco is None:
        endereco = os.path.basename(url.split("?")[0])
    resposta = requests.get(url, stream=True)
    if resposta.status_code == requests.codes.OK:
        with open(endereco, 'wb') as novo_arquivo:
            for parte in resposta.iter_content(chunk_size=256):
                novo_arquivo.write(parte)
        print("Download finalizado. Arquivo salvo em: {}".format(endereco))
    else:
        resposta.raise_for_status()
url = ''
baixar_arquivo(url)
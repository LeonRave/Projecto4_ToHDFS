import json
import hdfs
import time
import re

client = hdfs.InsecureClient('http://10.110.70.45:50070', user='root')

dir = 'twitter'

lista = client.list('/user/leon/'+dir+'/')

#regex=re.compile(".*_(VQ.).*")
#lista = [m.group(0) for l in lista for m in [regex.search(l)] if m]
#print(lista)

for twiit in lista:
	try:
		with client.read('/user/leon/'+dir+'/'+twiit, encoding='utf-8') as reader:
			model = json.load(reader)
		#print(json.loads(model)['user']['name'])
		a = json.loads(model)['text']
		if (a.find('Sismo')==-1):
			a=a
		else:
			print(json.loads(model)['text'])

		#print('/user/leon/'+dir+'/'+twiit)	
	except: 
		print('Archivo no pudo ser leido')

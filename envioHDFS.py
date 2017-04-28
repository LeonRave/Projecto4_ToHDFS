from kafka import KafkaConsumer
import json
import hdfs
import time

consumer = KafkaConsumer('topico', bootstrap_servers=['10.110.70.45:9092'])
client = hdfs.InsecureClient('http://10.110.70.45:50070', user='leon')

dir = 'twitter'

if(str(client.list('/')).find(dir)==-1):	
	client.makedirs('/user/leon/'+dir)	

for msg in consumer:
	twtJson = json.loads(msg.value.decode('utf8'))
	dumpsJson = json.dumps(msg.value.decode('utf8'))
	#print(twtJson)
	id = twtJson['id']
	mensaje = twtJson['text']
	usuario = twtJson['user']['name']
	created_at = twtJson['created_at']
	created_at = time.strftime('%d-%m-%Y', time.strptime(created_at,'%a %b %d %H:%M:%S +0000 %Y'))
	print(usuario)
	try:
		client.write('/user/leon/'+dir+'/'+str(id)+'_'+str(usuario)+'_'+str(created_at)+'.json', dumpsJson)
	except:
		print('No se pudo crear el archivo')



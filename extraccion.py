from kafka import KafkaProducer
import tweepy as tpy
import json

class Listener(tpy.StreamListener):

	def on_error(self, status_code):
		if status_code == 420:
			#returning False in on_data disconnects the stream
			return False

	def on_data(self, data):
		# Preparando datos para elastic
		raw = json.loads(data)
		data = json.dumps(raw, sort_keys =True, indent=4, separators=[",", ":"])
		print(raw['text'])

		#try:
		future = producer.send('topico', str.encode(data))
		#except:
		#	print("Error codif")
	

CONSUMER_KEY = 'p16pNm4jlUk2gxIVmRjlpBMgC'
CONSUMER_SECRET = 'aJj2lNUU6Z7CpPgqY58CBZfjhNskGSYfFkHeYrDfxynbDpMKaf'
ACCESS_KEY = '2191437690-c4tiRfmBV3NjuofnBK7ZnBkmLRSvNP90RrcQnWl'
ACCESS_SECRET = 'Wt613Xxw3Wozk30QttRVDr72VyXFVWGKbk6fLPTtkQgpd'

auth = tpy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.secure = True

auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tpy.API(auth)


print("===== Tweets en tiempo real =====")

#Start Producer
producer = KafkaProducer(bootstrap_servers='10.110.70.45:9092')

# Connect to the stream
print(">> Escuchando Twiiters:")
escucha  = Listener()
Stream = tpy.Stream(auth=api.auth, listener=escucha)
Stream.filter(track=['bbva', 'bancomer', 'hsbc', 'televisa', 'cnn'], languages=["es"])


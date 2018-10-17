import requests 
import json 
import glob
import  os
import json

cwd = os.getcwd()

for file in glob.glob(cwd + "/json_filtrage/*.json"):
	resultat = []
	file_name = file.split('/')[-1]


	with open(cwd + '/json_ready_semantique/' + file_name + '.json', 'w') as outfile:
		data = open(file).read()
		data = json.loads(data)
		try : 
			data_article = data[0]['article']
			response = requests.post(url = 'http://0.0.0.0:5005/filtering', json=data)
			id_article = response.json()[0][0]['message']['id_article']
			data[0]['article']['id_article'] = id_article
			resultat.append(data[0])
		except :
			print('no article')
		json.dump(resultat, outfile)
		
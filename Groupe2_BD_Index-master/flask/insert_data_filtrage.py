import requests 
import json 
import glob
import  os
cwd = os.getcwd()

import json





for file in glob.glob(cwd + "/json/*.json"):
	resultat = []
	file_name = file.split('/')[-1]


	with open(cwd + '/json_semantique/' + file_name + '.json', 'w') as outfile:
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
		
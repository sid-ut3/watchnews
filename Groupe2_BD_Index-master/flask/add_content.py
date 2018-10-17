import requests 
import json 
import glob
import  os
import json

cwd = os.getcwd()


for file in glob.glob(cwd + "/json_ready_semantique/*.json"):
	result = []
	#file_name = file.split('/')[-1]

	with open(file, 'r') as outfile:
		data = open(file).read()
		data = json.loads(data)
		file_name = file.split('/')[-1]
		try : 	
			for value in data[0]['position_word']:
				result.append(value['word'])
		except : 
			print('Key word is missing')

		try : 
			data[0]['content'] = {"words" : result}
			with open(cwd + '/json_ready_semantique_2/' + file_name, 'w') as outfile2:
				json.dump(data[0], outfile2)
		except : 
			print('key word missing')

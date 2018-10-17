import glob
import json

for file in glob.glob('In_Filtrage/*.json'):
    add = {'id_article' : i}
    with open(file, 'w') as f:
        f.write(json.dumps(add))
        f.close()
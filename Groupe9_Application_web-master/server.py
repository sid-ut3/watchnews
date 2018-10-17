# -*- coding: utf-8 -*-
"""
@author: G9
"""

from flask import Flask, request,  jsonify, Response
import json
from flask_restful import Resource, Api
import json
app = Flask(__name__)
api = Api(app)

 
##################################################
#					PAGE INDEX					 #   
##################################################
@app.route('/newspaper_by_article', methods = ['GET'])
def newspaper_by_article():
    data = {
   '1': {
        "newspaper": "figaro",
        "number_article" : 210
    },
    '2':{
        "newspaper": "monde",
        "number_article": 2015
    },
    '3':{
        "newspaper": "depeche",
        "number_article" : 50
    },
    '4':{
        "newspaper": "set",
        "number_article": 45
    },
    '5':{
        "newspaper": "truc",
        "number_article" : 544
    },
    '6':{
        "newspaper": "ouai",
        "number_article": 45
    },
    '7':{
        "newspaper": "plus",
        "number_article" : 76
    },
    '8':{
        "newspaper": "trente",
        "number_article": 71
    },
    '9':{
        "newspaper": "aller",
        "number_article" : 828
    },
    '10':{
        "newspaper": "dix",
        "number_article": 783
    },
    '11':{
        "newspaper": "onze",
        "number_article": 7823
    },
    '12':{
        "newspaper": "douze",
        "number_article": 78223
    }}
    resp = jsonify(data)
    resp.status_code = 200
    resp.headers.add('Access-Control-Allow-Origin', '*')
    return resp  
   
@app.route('/test1', methods = ['GET'])
def general1():
    data = {
    '1':{
        "text" : "Lorem",
        "weight" : 13,
        "trend": 'Strongly_increasing_trend'
    },
    '2':{
        "text" : "Ipsum",
        "weight" : 10.5,
        "trend": 'Increasing_trend'
    },
    '3':{
        "text" : "Dolor",
        "weight" : 9.4,
        "trend": 'No_trend'
    },
    '4':{
        "text" : "Sit",
        "weight" : 8,
        "trend": 'Decreasing_trend'
    },
    '5':{
        "text" : "Amet",
        "weight" : 6.2,
        "trend": 'Strongly_decreasing_trend'
    },
    '6':{
        "text" : "Consectetur",
        "weight" : 5,
        "trend": 'Increasing_trend'
    },
    '7':{
        "text" : "Adipiscing",
        "weight" : 5,
        "trend": 'Strongly_increasing_trend'
    },
    '8':{
        "text" : "Amzeet",
        "weight" : 7.2,
        "trend": 'Strongly_decreasing_trend'
    },
    '9':{
        "text" : "Conszezectetur",
        "weight" : 9,
        "trend": 'Increasing_trend'
    },
    '10':{
        "text" : "Adipzeiscing",
        "weight" : 5,
        "trend": 'Strongly_increasing_trend'
    }}
    resp = jsonify(data)
    resp.status_code = 200
    resp.headers.add('Access-Control-Allow-Origin', '*')
    return resp


@app.route('/best_label_week', methods = ['GET'])
def best_label_week():
    data = {
   '1': {
        "label": "France",
        "ratio_article" : "50%"
    }}
    resp = jsonify(data)
    resp.status_code = 200
    resp.headers.add('Access-Control-Allow-Origin', '*')
    return resp 

@app.route('/top_3_rate_feeling', methods = ['GET'])
def top_3_rate_feeling():
	data = {
	'1': {
		"feeling": "Degout",
		"rate" : "0.5"
	},
	'2': {
		"feeling": "Peur",
		"rate" : "0.8"
	},
	'3': {
		"feeling": "Joie",
		"rate" : "0.2"
	}}
	resp = jsonify(data)
	resp.status_code = 200
	resp.headers.add('Access-Control-Allow-Origin', '*')
	return resp 


##################################################
#					PAGE THEME					#   
##################################################


@app.route('/newspaper_by_label', methods = ['GET'])
def newspaper_by_label():
    data = {
	'1':{
		"label" : "Art et Culture",
		"number_article" : 31090763
	},
	'2':{
		"label" : "Economie",
		"number_article" : 61801570
	},
	'3':{
		"label" : "Science",
		"number_article" : 73137148
	},
	'4':{
		"label" : "Sports",
		"number_article" : 74856000
	},
	'5':{
		"label" : "France",
		"number_article" : 79716203
	},
	'6':{
		"label" : "International",
		"number_article" : 81902307
	},
	'7':{
		"label" : "Santé",
		"number_article" : 141850000
	}}
    resp = jsonify(data)
    resp.status_code = 200
    resp.headers.add('Access-Control-Allow-Origin', '*')
    return resp

@app.route('/link_by_tagging/<string:vparam1>', methods = ['GET'])
def link_by_tagging(vparam1):
    #theme =request.args.get('theme')
    print(vparam1)
    data_first = {
    '1':{
    	"text" : "Verbe",
        "type" : "VERB",
        "trend" : "Increasing_trend"
    },
    '2':{
    	"text" : "Nom propre",
        "type" : "PROPER_NOUN",
        "trend" : "Decreasing_trend"
    },
    '3':{
    	"text" : "Adjectif",
        "type" : "ADJECTIVE",
        "trend" : "No_trend"
    }}
    data_bis = {
    '1':{
    	"text" : "Manger",
        "type" : "VERB",
        "trend" : "Increasing_trend"
    },
    '2':{
    	"text" : "Donald Trump",
        "type" : "PROPER_NOUN",
        "trend" : "Decreasing_trend"
    },
    '3':{
    	"text" : "Gros",
        "type" : "ADJECTIVE",
        "trend" : "Increasing_trend"
    }}
    data_ter = {
    '1':{
    	"text" : "Boire",
        "type" : "VERB",
        "trend" : "Strongly_increasing_trend"
    },
    '2':{
    	"text" : "Individu",
        "type" : "PROPER_NOUN",
        "trend" : "Strongly_decreasing_trend"
    },
    '3':{
    	"text" : "Savoureux",
        "type" : "ADJECTIVE",
        "trend" : "No_trend"
    }}
    if vparam1 == 'international':
        data = data_first
    elif vparam1 == 'france':
        data = data_bis
    else:
        data = data_ter
    resp = jsonify(data)
    resp.status_code = 200
    resp.headers.add('Access-Control-Allow-Origin', '*')
    return resp

@app.route('/link_by_label/<string:vparam1>', methods = ['GET'])
def link_by_label(vparam1):
    print(vparam1)
    data_first = {
    '1':{
        "text" : "Lorem",
        "weight" : 13,
        "trend": 'Strongly_increasing_trend'
    },
    '2':{
        "text" : "Ipsum",
        "weight" : 10.5,
        "trend": 'Increasing_trend'
    },
    '3':{
        "text" : "Dolor",
        "weight" : 9.4,
        "trend": 'No_trend'
    },
    '4':{
        "text" : "Sit",
        "weight" : 8,
        "trend": 'Decreasing_trend'
    },
    '5':{
        "text" : "Amet",
        "weight" : 6.2,
        "trend": 'Strongly_decreasing_trend'
    },
    '6':{
        "text" : "Consectetur",
        "weight" : 5,
        "trend": 'Increasing_trend'
    },
    '7':{
        "text" : "Adipiscing",
        "weight" : 5,
        "trend": 'Strongly_increasing_trend'
    }}
    data_bis = {
    '1':{
        "text" : "Arbre",
        "weight" : 13,
        "trend": 'No_trend'
    },
    '2':{
        "text" : "Bol",
        "weight" : 10.5,
        "trend": 'Increasing_trend'
    },
    '3':{
        "text" : "Cerceau",
        "weight" : 9.4,
        "trend": 'Strongly_decreasing_trend'
    },
    '4':{
        "text" : "Domino",
        "weight" : 8,
        "trend": 'No_trend'
    },
    '5':{
        "text" : "Elephant",
        "weight" : 6.2,
        "trend": 'Decreasing_trend'
    },
    '6':{
        "text" : "Fabriquer",
        "weight" : 5,
        "trend": 'No_trend'
    },
    '7':{
        "text" : "Gateau",
        "weight" : 5,
        "trend": 'Strongly_increasing_trend'
    }}
    data_ter = {
    '1':{
        "text" : "Hibou",
        "weight" : 13,
        "trend": 'Strongly_increasing_trend'
    },
    '2':{
        "text" : "Important",
        "weight" : 10.5,
        "trend": 'Decreasing_trend'
    },
    '3':{
        "text" : "Joyeux",
        "weight" : 9.4,
        "trend": 'Decreasing_trend'
    },
    '4':{
        "text" : "Lalala",
        "weight" : 8,
        "trend": 'Increasing_trend'
    },
    '5':{
        "text" : "Mouton",
        "weight" : 6.2,
        "trend": 'Strongly_decreasing_trend'
    },
    '6':{
        "text" : "Négation",
        "weight" : 5,
        "trend": 'Increasing_trend'
    },
    '7':{
        "text" : "Obligation",
        "weight" : 5,
        "trend": 'No_trend'
    }}
    if vparam1 == 'international':
        data = data_first
    elif vparam1 == 'france':
        data = data_bis
    else:
        data = data_ter
    resp = jsonify(data)
    resp.status_code = 200
    resp.headers.add('Access-Control-Allow-Origin', '*')
    return resp

##################################################
#					PAGE RECHERCHE				#   
##################################################

@app.route('/article_per_day_source/<string:vparam1>/<string:vparam2>/<string:vparam3>', methods = ['GET'])
def article_per_day_source(vparam1,vparam2,vparam3):
	print(vparam1,vparam2,vparam3)
	data = {
	'1':{
		"date" : "w1",
		"newspaper" : "La Dépêche",
		"number_article" : 10
	},
	'2':{
		"date" : "w1",
		"newspaper" : "Le Figaro",
		"number_article" : 1
	},
	'3':{
		"date" : "w1",
		"newspaper" : "Le Point",
		"number_article" : 12
	},
	'4':{
		"date" : "w1",
		"newspaper" : "Le Monde",
		"number_article" : 2
	},
	'5':{
		"date" : "w1",
		"newspaper" : "Libération",
		"number_article" : 9
	},
	'6':{
		"date" : "w1",
		"newspaper" : "Nouvelle Obs",
		"number_article" : 13
	},
	'7':{
		"date" : "w1",
		"newspaper" : "Telerama",
		"number_article" : 6
	},
	'8':{
		"date" : "w1",
		"newspaper" : "Futurasciences",
		"number_article" : 5
	},
	'9':{
		"date" : "w1",
		"newspaper" : "L’Humanité",
		"number_article" : 9
	},
	'10':{
		"date" : "w2",
		"newspaper" : "La Dépêche",
		"number_article" : 20
	},
	'11':{
		"date" : "w2",
		"newspaper" : "Le Figaro",
		"number_article" : 35
	},
	'12':{
		"date" : "w2",
		"newspaper" : "Le Point",
		"number_article" : 15
	},
	'13':{
		"date" : "w2",
		"newspaper" : "Le Monde",
		"number_article" : 17
	},
	'14':{
		"date" : "w2",
		"newspaper" : "Libération",
		"number_article" : 3
	},
	'15':{
		"date" : "w2",
		"newspaper" : "Nouvelle Obs",
		"number_article" : 22
	},
	'16':{
		"date" : "w2",
		"newspaper" : "Telerama",
		"number_article" : 8
	},
	'17':{
		"date" : "w2",
		"newspaper" : "Futurasciences",
		"number_article" : 3
	},
	'18':{
		"date" : "w2",
		"newspaper" : "L’Humanité",
		"number_article" : 6
	},
	'19':{
		"date" : "w3",
		"newspaper" : "La Dépêche",
		"number_article" : 15
	},
	'20':{
		"date" : "w3",
		"newspaper" : "Le Figaro",
		"number_article" : 5
	},
	'21':{
		"date" : "w3",
		"newspaper" : "Le Point",
		"number_article" : 11
	},
	'22':{
		"date" : "w3",
		"newspaper" : "Le Monde",
		"number_article" : 17
	},
	'23':{
		"date" : "w3",
		"newspaper" : "Libération",
		"number_article" : 7
	},
	'24':{
		"date" : "w3",
		"newspaper" : "Nouvelle Obs",
		"number_article" : 23
	},
	'25':{
		"date" : "w3",
		"newspaper" : "Telerama",
		"number_article" : 28
	},
	'26':{
		"periode" : "w3",
		"newspaper" : "Futurasciences",
		"number_article" : 13
	},
	'27':{
		"date" : "w3",
		"newspaper" : "L’Humanité",
		"number_article" : 9
	}}
	resp = jsonify(data)
	resp.status_code = 200
	resp.headers.add('Access-Control-Allow-Origin', '*')
	return resp 


@app.route('/article_per_day_label/<string:vparam1>/<string:vparam2>/<string:vparam3>', methods = ['GET'])
def article_per_day_label(vparam1,vparam2,vparam3):
	print(vparam1,vparam2,vparam3)
	data = {
	'1':{
		"date" : "w1",
		"label" : "France",
		"number_article" : 10
	},
	'2':{
		"date" : "w1",
		"label" : "Internationale",
		"number_article" : 1
	},
	'3':{
		"date" : "w1",
		"label" : "Sport",
		"number_article" : 12
	},
	'4':{
		"date" : "w1",
		"label" : "Santé",
		"number_article" : 2
	},
	'5':{
		"date" : "w1",
		"label" : "Culture",
		"number_article" : 9
	},
	'6':{
		"date" : "w1",
		"label" : "Economie",
		"number_article" : 13
	},
	'7':{
		"date" : "w1",
		"label" : "Science/High-Tech",
		"number_article" : 6
	},
	'8':{
		"date" : "w2",
		"label" : "France",
		"number_article" : 5
	},
	'9':{
		"date" : "w2",
		"label" : "Internationale",
		"number_article" : 9
	},
	'10':{
		"date" : "w2",
		"label" : "Sport",
		"number_article" : 20
	},
	'11':{
		"date" : "w2",
		"label" : "Santé",
		"number_article" : 35
	},
	'12':{
		"date" : "w2",
		"label" : "Culture",
		"number_article" : 15
	},
	'13':{
		"date" : "w2",
		"label" : "Economie",
		"number_article" : 17
	},
	'14':{
		"date" : "w2",
		"label" : "Science/High-Tech",
		"number_article" : 3
	},
	'15':{
		"date" : "w3",
		"label" : "France",
		"number_article" : 22
	},
	'16':{
		"date" : "w3",
		"label" : "Internationale",
		"number_article" : 8
	},
	'17':{
		"date" : "w3",
		"label" : "Sport",
		"number_article" : 3
	},
	'18':{
		"date" : "w3",
		"label" : "Santé",
		"number_article" : 6
	},
	'19':{
		"date" : "w3",
		"label" : "Culture",
		"number_article" : 15
	},
	'20':{
		"date" : "w3",
		"label" : "Economie",
		"number_article" : 5
	},
	'21':{
		"date" : "w3",
		"label" : "Science/High-Tech",
		"number_article" : 11
	}}
	resp = jsonify(data)
	resp.status_code = 200
	resp.headers.add('Access-Control-Allow-Origin', '*')
	return resp 


@app.route('/article_per_source/<string:vparam1>/<string:vparam2>/<string:vparam3>', methods = ['GET'])
def article_per_source(vparam1,vparam2,vparam3):
	print(vparam1,vparam2,vparam3)
	data = {
	'1':{
		"newspaper" : "La Dépêche",
		"number_article" : 50
	},
	'2':{
		"newspaper" : "Le Figaro",
		"number_article" : 210
	},
	'3':{
		"newspaper" : "Le Point",
		"number_article" : 12
	},
	'4':{
		"newspaper" : "Le Monde",
		"number_article" : 2015
	},
	'5':{
		"newspaper" : "Libération",
		"number_article" : 45
	},
	'6':{
		"newspaper" : "Nouvelle Obs",
		"number_article" : 544
	},
	'7':{
		"newspaper" : "Telerama",
		"number_article" : 45
	},
	'8':{
		"newspaper" : "Futurasciences",
		"number_article" : 76
	},
	'9':{
		"newspaper" : "L’Humanité",
		"number_article" : 71
	}}
	resp = jsonify(data)
	resp.status_code = 200
	resp.headers.add('Access-Control-Allow-Origin', '*')
	return resp 
	
@app.route('/article_per_label/<string:vparam1>/<string:vparam2>/<string:vparam3>', methods = ['GET'])
def article_per_label(vparam1,vparam2,vparam3):
	print(vparam1,vparam2,vparam3)
	data = {
	'1':{
		"label" : "France",
		"number_article" : 50
	},
	'2':{
		"label" : "Internationale",
		"number_article" : 210
	},
	'3':{
		"label" : "Sport",
		"number_article" : 12
	},
	'4':{
		"label" : "Santé",
		"number_article" : 2015
	},
	'5':{
		"label" : "Culture",
		"number_article" : 45
	},
	'6':{
		"label" : "Economie",
		"number_article" : 544
	},
	'7':{
		"label" : "Science/High-Tech",
		"number_article" : 45
	}}
	resp = jsonify(data)
	resp.status_code = 200
	resp.headers.add('Access-Control-Allow-Origin', '*')
	return resp 

@app.route('/article_per_day/<string:vparam1>/<string:vparam2>/<string:vparam3>', methods = ['GET'])
def article_per_day(vparam1,vparam2,vparam3):
	print(vparam1,vparam2,vparam3)
	data = {
	'1':{
		"date" : "w1",
		"number_article" : 10
	},
	'2':{
		"date" : "w2",
		"number_article" : 12
	},
	'3':{
		"date" : "w3",
		"number_article" : 12
	}}
	resp = jsonify(data)
	resp.status_code = 200
	resp.headers.add('Access-Control-Allow-Origin', '*')
	return resp 

@app.route('/positivity_per_newspaper/<string:vparam1>/<string:vparam2>/<string:vparam3>', methods = ['GET'])
def positivity_per_newspaper(vparam1,vparam2,vparam3):
	print(vparam1,vparam2,vparam3)
	data = {
	'1':{
		"source" : "La Dépêche",
		"polarite" : 0
	},
	'2':{
		"source" : "Le Figaro",
		"polarite" : 0.1
	},
	'3':{
		"source" : "Le Point",
		"polarite" : 0.54
	},
	'4':{
		"source" : "Le Monde",
		"polarite" : 1
	},
	'5':{
		"source" : "Libération",
		"polarite" : 0.98
	},
	'6':{
		"source" : "Nouvelle Obs",
		"polarite" : 0.06
	},
	'7':{
		"source" : "Telerama",
		"polarite" : 0.23
	},
	'8':{
		"source" : "Futurasciences",
		"polarite" : 0.56
	},
	'9':{
		"source" : "L’Humanité",
		"polarite" : 1
	}}
	resp = jsonify(data)
	resp.status_code = 200
	resp.headers.add('Access-Control-Allow-Origin', '*')
	return resp 



@app.route('/found_word/<string:vparam1>', methods = ['GET'])
def found_word(vparam1):
	print(vparam1)
	data = {
	'1':{
		"word" : "Donald_Trump",
		"link" : "https://fr.wikipedia.org/wiki/Donald_Trump"
	}}
	resp = jsonify(data)
	resp.status_code = 200
	resp.headers.add('Access-Control-Allow-Origin', '*')
	return resp 

if __name__ == '__main__':
  app.run(debug=True)
  

from elasticsearch import Elasticsearch
from pymongo import MongoClient
import json

#Elasticsearch mapping
mapping = { "fulltext" :  {
		"_all" :  {
		"analyzer" : "ik_max_word",
		"search_analyzer" : "ik_max_word",
		"term_vector" : "no",
		"store" : "false"
		},  
		 "properties" : {
		    "content" :  {
 			"type" : "string",
			"store" : "no",
			"term_vector" : "with_positions_offsets",
			"analyzer" : "ik_max_word",
			"search_analyzer" : "ik_max_word",
			"include_in_all" : "true",
			"boost" : 7
		},
		    "title" : {
			"type" : "string",
			"store" : "no",
			"term_vector" : "with_positions_offsets",
			"analyzer" : "ik_max_word",
			"search_analyzer" : "ik_max_word",
			"include_in_all" : "true",
			"boost" : 8
		},
		    "link" : {
			"type" : "string",
			"store" : "no",
			"index" : "not_analyzed"
		}
	     }
	}
}	

##Convert Mongodb data to JSON
def to_es_json(bson):
    data = {
	'title' : bson['title'],
	'content' : bson['content'],
	'link' : bson['link']
    }
    return json.dumps(data)

es = Elasticsearch('http://localhost:9200')
es.indices.create('search', body={"mappings" : mapping})

client = MongoClient('localhost',27017)
db = client['examdb']
document = db['search']

#print result
i = 0
for doc in document.find():
	res = to_es_json(doc)
	es.create('search',doc_type="fulltext",body=res)
	i += 1

print i

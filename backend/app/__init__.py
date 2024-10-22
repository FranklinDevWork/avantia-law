from flask import Flask

app = Flask(__name__)

from elasticsearch import Elasticsearch, helpers
import json

es = Elasticsearch(
    "http://elasticsearch:9200/",
    http_auth=("elastic", "password")
)

with open("./app/prize.json", "r", encoding="utf8") as file:
    data = json.load(file)
    for idx, prize in enumerate(data["prizes"]):
        doc = json.dumps(prize)
        resp = es.index(index="prizes", id=idx, body=doc)
        print(resp["result"])

from app import routes
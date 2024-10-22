from app import app
from flask import Flask, request

from elasticsearch import Elasticsearch, helpers
import json

es = Elasticsearch(
    "http://elasticsearch:9200/",
    http_auth=("elastic", "password")
)

@app.route('/')
@app.route('/index')
def index():
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
    return "Hello, World!"

@app.route('/search', methods=['GET'])
def search():
    args = request.args
    name = args.get("name", None)
    if name is not None:
        query={
            "query": {
                "match": {
                "laureates.firstname": name
                }
            }
        }
        result = es.search(index="prizes", body=query)
        return result
    return ""
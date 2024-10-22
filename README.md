# avantia-law

This is the assignment for a role at avantia law. It is a python flask API using elastic search.

## Running

```
docker-compose up --build
```

This should launch both the backend services and API is on port 5000.

## Endpoints

```
curl localhost:5000/search?name=albert
```

## Missing

* Searching by description
* Ranking

## Troubleshooting

If there is no data in the ES cluster, hit the following and wait till completion

```
curl localhost:5000/
```
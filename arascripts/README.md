## Mongo DB for the Allen Research Atlas

These are scripts to help import and query the ARA.

* Files
  * ara.json -- input file downloaded from Allen.  Whole atlas as a single object
  * parser_ara.py -- convert ara.json into format suitable for mongo ingest
  * ara.mongo.ingest.json -- output of parseara.py
  * index_ara.py -- build indexes for id (and children?)

* Commands
  * bulk ingest a database from ARA 
```mongoimport --db atlases --collection ara --drop --file ./ara.mongo.ingest.json``` 
 


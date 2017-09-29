## Mongo DB for the Waxholm Rat Atlas

These are scripts to help import and query the ARA.

* Files
  * WHS_SD_rat_atlas_v2_labels.ilf -- input file downloaded from Allen.  Whole atlas as a single object
  * parser_whs.py -- convert into format suitable for mongo ingest
  * whs.mongo.ingest.json -- output of parseara.py
  * index_whs.py -- build indexes for id (and children?)

* Commands
  * bulk ingest a database from ARA 
```mongoimport --db atlases --collection whs --drop --file ./whs.mongo.ingest.json``` 
 


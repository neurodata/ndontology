#!/bin/bash
python3 parse_whs.py
mongoimport --db atlases --collection whs --drop --file ./whs.mongo.ingest.json
python3 index_whs.py
python3 nametree_whs.py

#!/bin/bash
python3 parse_ara.py
mongoimport --db atlases --collection ara --drop --file ./ara.mongo.ingest.json
python3 index_ara.py
python3 nametree_ara.py

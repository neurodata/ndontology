# ndaraontology
Manage/query/update a MongoDB in Docker that contains the 
* Allen Research Atlas Ontology
* Waxholm Rat Atlas.

These tools run in python 3.5+, require a mongo database to talk to.
You need to install a late version of mongo clients (3.4.9).
Please `pip/pip3 install -r requirements.txt` to configure your python or virtualenv.

See README.md in ./docker for run instructions
    

The docker-compose file will load the databases.  It can be done manually on any running mongo instance.

```
Run the load scripts to put ontology databases onto local mongodb.  You need to have PTYHONPATH set to the root directory of this repository, e.g. /home/XXXX/ndontology
```
    cd arascripts
    ./load_ara.sh
    cd ../whsscripts
    ./load_whs.sh
    cd ..
```
Run the unit tests
```
    py.test 
```

## What you get

A MongoDB instance running in docker that has the following databases:
* Allen Reference Atlas
    * atlases.ara -- DB of ROIs supports lookup by id, atlas\_id, details, and descendants
    * atlases.ara\_nametree -- contains one object with hierarchical tree of all objects
* Waxholm Rat Atlas
    * atlases.whs -- DB of ROIs supports lookup by id, details, and descendants
    * atlases.whs\_nametree -- contains one object with hierarchical tree of all objects

Reference queries are in the unit tests and ontology.py/araonotology.py

All of the tests and reference queries assume that Mongo runs on localhost.

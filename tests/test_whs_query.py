# Copyright 2014 NeuroData (http://neurodata.io)
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pytest
from datetime import datetime
import json
from jsondiff import diff
from pymongo import MongoClient

from ndontology import NDOntology

@pytest.fixture()
def whsont_object():
    """A fixture that loads the database."""
    whsont = NDOntology ( "atlases", "whs", "mongodb://localhost:27017" )
    yield whsont


class TestWHSOntology():
    
    def test_id_query(self, whsont_object):
        """Query for single fields"""
        roi = whsont_object.query_by_id(49) 
        assert(roi['id'] == 49)
        assert(roi['name'] == 'inferior colliculus')

        roi = whsont_object.query_by_id(1002) 
        assert(roi['children'] == [6, 38, 52, 59])

    def test_descendants(self, whsont_object):
        "Query subtree"
        roi = whsont_object.descendants(1010)

        assert(roi['id'] == 1010)
        assert(97 in roi['descendants'])
        assert(len(roi['depth']) == 48)

    def test_name_tree(self, whsont_object):
        "Tree hierarchy for d3js"""
        name_tree = whsont_object.name_tree(99999)
        # compare against stored name tree
        collection = MongoClient().atlases.whs_nametree 
        store_tree = collection.find_one()
        store_tree.pop("_id")
        assert(json.dumps(name_tree) == json.dumps(store_tree))

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

from araontology import ARAOntology

@pytest.fixture()
def araont_object():
    """A fixture that loads the database."""
    araont = ARAOntology ( "atlases", "ara", "mongodb://localhost:27017" )
    yield araont


class TestARAOntology():
    
    def test_id_query(self, araont_object):
        """Query for single fields"""
        roi = araont_object.query_by_id(1000) 
        assert(roi['id'] == 1000)
        assert(roi['name'] == 'extrapyramidal fiber systems')

        roi = araont_object.query_by_id(997) 
        assert(roi['children'] == [8, 1009, 73, 1024, 304325711])

    def test_atlas_id_query(self, araont_object):
        """Query for single fields"""
        roi = araont_object.query_by_atlas_id(253) 
        assert(roi['atlas_id'] == 253)
        assert(roi['name'] == 'Pontine central gray')

    def test_descendants(self, araont_object):
        "Query subtree"
        roi = araont_object.descendants(528)

        assert(roi['id'] == 528)
        assert(10716 in roi['descendants'])
        assert(len(roi['depth']) == 80)

    def test_name_tree(self, araont_object):
        "Tree hierarchy for d3js"""
        roi = araont_object.name_tree(528)
        import pdb; pdb.set_trace()

    def test_rebuild(self, araont_object):
        """Rebuild the same file as input"""
        roi = araont_object.ara_ontology() 
        fp = open("scripts/ara.json")
        oldjsons = json.dumps(json.load(fp)['msg'][0])
        newjsons = json.dumps(roi[0])
        assert(oldjsons== newjsons)
      
#        assert(roi[0]['id'] == oldjson['msg'][0]['id'])
#        print( diff(roi[0],oldjson['msg'][0]) )

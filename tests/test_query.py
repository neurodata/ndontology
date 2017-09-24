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

from araontology import ARAOntology

@pytest.fixture()
def araont_object():
    """A fixture that loads the database."""
    araont = ARAOntology ( "atlases", "ara", "mongodb://localhost:27017" )
    yield araont

class TestARAOntology():

    def test_stabbing_query(self, araont_object):
        """Query for single fields"""

        roi = araont_object.query_by_id(1000) 
        assert(roi['id'] == 1000)
        assert(roi['name'] == 'extrapyramidal fiber systems')

        roi = araont_object.query_by_id(997) 
        assert(roi['children'] == [8, 1009, 73, 1024, 304325711])

    def test_tree_query(self, araont_object):

        import pdb; pdb.set_trace()
        roi = araont_object.query_tree(528)

        assert(roi['id'] == 528)
        assert(10716 in roi['descendants'])
        assert(len(roi['depth']) == 80)

        


        

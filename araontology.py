# Copyright 2017 NeuroData (http://neurodata.io)
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

from pymongo import MongoClient

class ARAOntology:
    """Manage a MongoDB that contains the Allen Research Atlas Ontology.
        This database should have been ingested from the tools in ndaraontology/scripts"""

    def __init__(self, database_name: str, collection_name: str, uri: str=None ) -> None:
        """ Create a connection to the MongoDB:
        
            Parameters:
                uri -- uri to Mongo instance
                database_name -- name of database 
                collection_name -- name of collection

            Returns: None
        """
        self.client = MongoClient ( uri )
        self.db = self.client[database_name]
        self.collection = self.db[collection_name]

    def query_by_id(self, roi_id: int) -> dict:
        """Fetch and return the dictionary entry describing a ROI in the ARA by id

            Parameters:
                roi_id -- identifier

            Returns: dictionary of the ARA specified fields
        """
        return self.collection.find_one({"id": roi_id})

    def query_by_atlas_id(self, roi_id: int) -> dict:
        """Fetch and return the dictionary entry describing a ROI in the ARA by id

            Parameters:
                roi_id -- identifier

            Returns: dictionary of the ARA specified fields
        """
        return self.collection.find_one({"atlas_id": roi_id})

    def descendants (self, roi_id: int) -> dict:
        """Find all descendants of the specified roi

            Parameters:
                roi_id -- identifier

            Returns: dictionary that contains
                roi_id -- parent identifier
                descendants -- list of ids of all children/descendants
                depth -- list of level (0 for direct children, 1 for grandchildren, ...)
        """
        # query tree with graphlookup pipeline
        treecursor = self.collection.aggregate([
            { "$match": { "id": roi_id }},
            { "$graphLookup":
                { "from": self.collection.name,
                  "startWith": "$children",
                  "connectFromField": "children",
                  "connectToField": "id",
                  "maxDepth": 8,
                  "as": "roitree",
                  "depthField": "depth"
                }
           },
           { "$project" :
               { "_id": 0,
                 "id" : 1,
                 "descendants": "$roitree.id",
                 "depth": "$roitree.depth"
               }
           }
        ])

        # return first element (should be only one)
        for roi in treecursor:
            return roi
        # return None if not found
        return None

    def _output_name(self, roi_id: int, ara_list: list) -> None:
        """Recursive call to help with name_tree"""

        aradict = {}

        # add fields to dictionary
        roi = self.collection.find_one({"id": roi_id})
        aradict["id"]=roi["id"]
        aradict["name"] = roi["name"]


        # recursively call for all children
        aradict['children']= []
        
        for roi_id in roi['children']:
            ret_dict = self._output_name(roi_id,aradict['children']) 

        ara_list.append(aradict)

    def name_tree (self, roi_id: int) -> dict:
        """Return a name tree hierarchy for JSON

            Parameters:
                roi_id -- identifier

            Returns: dictionary that contains
                roi_id -- parent identifier
                descendants -- list of ids of all children/descendants
                depth -- list of level (0 for direct children, 1 for grandchildren, ...)
        """
        name_tree = []
        self._output_name (roi_id, name_tree)

        return name_tree[0] 

# RB would like to dod this with graphLookup but can't get the
#   $project part of the query to be applied recursively
#   this query without project returns all fields as we want them
#
#        # query tree with graphlookup pipeline
#        treecursor = name_view.aggregate([
#            { "$match": { "id": roi_id }},
#            { "$graphLookup":
#                { "from": self.collection.name,
#                  "startWith": "$children",
#                  "connectFromField": "children",
#                  "connectToField": "id",
#                  "maxDepth": 8,
#                  "as": "roitree",
#                }
#           },
#           { "$project": 
#                {
#                }                            
#           }
#        ])

        # return first element (should be only one)
        for roi in treecursor:
            return roi
        # return None if not found
        return None




    def _output_roi(self, roi_id: int, ara_list: list) -> None:
        """Recursive call to help with ara_ontology"""

        aradict = {}

        # add fields to dictionary
        roi = self.collection.find_one({"id": roi_id})
        aradict["id"]=roi["id"]
        aradict["atlas_id"] = roi["atlas_id"]
        aradict["ontology_id"] = roi["ontology_id"]
        aradict["acronym"] = roi["acronym"]
        aradict["name"] = roi["name"]
        aradict["color_hex_triplet"] = roi["color_hex_triplet"]
        aradict["graph_order"] = roi["graph_order"] 
        aradict["st_level"] = roi["st_level"]
        aradict["hemisphere_id"] = roi["hemisphere_id"]
        aradict["parent_structure_id"] = roi["parent_structure_id"]


        # recursively call for all children
        aradict['children']= []
        
        for roi_id in roi['children']:
            ret_dict = self._output_roi(roi_id,aradict['children']) 

        ara_list.append(aradict)
            
        
    def ara_ontology(self):
        """Rebuild the ara file that we ingested.  Inline the objects.

            Parameters: None

            Returns: dictionary 
        """
        ara_msg=[]

        self._output_roi(997, ara_msg)
        return ara_msg

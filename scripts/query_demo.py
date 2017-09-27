import json

from araontology import ARAOntology

araont = ARAOntology ( "atlases", "ara", "mongodb://localhost:27017" )

root_tree = araont.query_tree(997)

for roi_id in root_tree['descendants']:
    roi =  araont.query_by_id(roi_id)
    print("Query by ROI", roi)
    if not roi['atlas_id'] is None:
        atlas_roi =  araont.query_by_id(roi['atlas_id'])
        print("Same by atlas ID", atlas_roi)
#    print("ROI ID {}, type {}".format(roi['n']['id'], synapse['synapse']['type']))

for roi_id in root_tree['descendants']:
    sub_tree = araont.query_tree(roi_id)
    print("Descendants of {} = {}", sub_tree['descendants'])

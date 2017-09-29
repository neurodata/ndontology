import json
import xmltodict
from queue import Queue

with open('WHS_SD_rat_atlas_v2_labels.ilf') as fd:
    whs_dict = xmltodict.parse(fd.read())

whs_atlas = whs_dict['milf']['structure']['label']
ofp = open('whs.mongo.ingest.json', "w")

# make a root to connect the forest
mongodata = {}
mongodata['id'] = int(99999)
mongodata['name'] = 'root'
mongodata['color'] = '#000000'
mongodata['children'] = []
for i in range(len(whs_atlas)):
    mongodata['children'].append(int(whs_atlas[i]['@id']))
print(mongodata['children'])
json.dump(mongodata, ofp)
    
roiqueue = Queue()

for i in range(len(whs_atlas)):

    roiqueue.put(whs_atlas[i])

    while not roiqueue.empty(): 
        roi = roiqueue.get()
        mongodata['id'] = int(roi['@id'])
        mongodata['name'] = roi['@name']
        mongodata['color'] = roi['@color']
        mongodata['children'] = []
        if 'label' in roi:
            for child in roi['label']:
                mongodata['children'].append(int(child['@id']))
                roiqueue.put(child)

        json.dump(mongodata, ofp)

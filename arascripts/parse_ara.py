import json
from queue import Queue

fp = open('ara.json')
araont = json.load(fp)

ofp = open('ara.mongo.ingest.json', "w")

mongodata = {}

roiqueue = Queue()
roiqueue.put(araont['msg'][0])

#while roiqueue:
#    k,v = roiqueue.pop()

while not roiqueue.empty(): 
    roi = roiqueue.get()
    for k,v in roi.items():

        # process all children first (preorder)
        if not k == 'children':
            mongodata[k] = v
        else:
            mongodata['children'] = []
            for nextroi in v:
                mongodata['children'].append(nextroi['id'])
                roiqueue.put(nextroi)

    json.dump(mongodata, ofp)

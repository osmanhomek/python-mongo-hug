import hug
import sections
import pymongo
import json
import bson

from pymongo import MongoClient
from bson import json_util, ObjectId
#from bson.json_util import dumps

def getSections(aid: hug.types.text):
    #aid : application_id
    
    #http://54.166.161.36:8000/getSections/57fbd3c17d2ba5447f72c796
    try:
        client = MongoClient('mongodb://usr_gunde_5dk:Rrd3b7yk28rbAwZb@ds035036.mlab.com:35036/gunde5dkcom')
        db = client.gunde5dkcom
    
        sectionsInfo = json.loads(json_util.dumps({'sections': []}))
        
        resultSections = db.applications.find({"_id":ObjectId(aid)})
        if resultSections.count()>0:
            section_ids  = resultSections[0]["section_id"]
            resultSectionInfo = db.sections.find({"_id":{'$in':section_ids}}, {"order":0,"card_id":0}).sort('order',pymongo.ASCENDING)
            if resultSectionInfo.count()>0:
                sectionsInfo = json.loads(json_util.dumps({'sections': resultSectionInfo}))
            else:
                sectionsInfo = json.loads(json_util.dumps({'sections': []}))
        else:
            sectionsInfo = json.loads(json_util.dumps({'sections': []}))
    except bson.errors.InvalidId:
        #gonderilen ID ObjectID tipinde degils
        pass
    
    client.close()

    return sectionsInfo
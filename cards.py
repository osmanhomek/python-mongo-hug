import hug
import cards
import pymongo
import json
import bson

from pymongo import MongoClient
from bson import json_util, ObjectId
from datetime import datetime

def getUnviewedCards(uid:hug.types.text,aid:hug.types.text,pid:hug.types.text,sid:hug.types.text,):
    #uid : user_id
    #aid : application_id
    #pid : package_id
    #sid : section_id
    
    #/getUnviewedCards/57f57781f807e512cdbd7325/57fbe0ee7d2ba5447f72c7d0
    
    limitval = 5
    try:
        client = MongoClient('mongodb://usr_gunde_5dk:Rrd3b7yk28rbAwZb@ds035036.mlab.com:35036/gunde5dkcom')
        db = client.gunde5dkcom
    
        UnviewdCardsInfo = json.loads(json_util.dumps({'cards': []}))
        
        result_viewed_cards = db.lpath.find({
            "user_id":ObjectId(pid),
            "section_id":ObjectId(id)
        }, {"_id":0, "viewed_card_ids":1 }).limit(1)
        if result_viewed_cards.count()>0:
            viewed_card_ids = result_viewed_cards[0]["viewed_card_ids"]
            unviewed_card_ids = db.cards.find({"section_id":ObjectId(id),"_id":{"$nin":viewed_card_ids}}, {"section_id":0}).limit(limitval)
            UnviewdCardsInfo = json.loads(json_util.dumps({'cards': unviewed_card_ids}))
    
        client.close()
    except bson.errors.InvalidId:
        #gonderilen ID ObjectID tipinde degils
        pass
    
    return UnviewdCardsInfo

def insViewedCard(uid:hug.types.text,aid:hug.types.text,pid:hug.types.text,sid:hug.types.text,cid:hug.types.text):
    #uid : user_id
    #aid : application_id
    #pid : package_id
    #sid : section_id
    #cid : card_id
    result_viewed_cards = db.lpath.find({"user_id":ObjectId(pid),"section_id":ObjectId(id)}, {"_id":0, "viewed_card_ids":1 }).limit(1)
    if result_viewed_cards.count()>0:
        #update
        pass
    else:
        #insert
        """
        result = db.lpath.insert_one({
            "user_id": ObjectId(uid),
            "application_id": ObjectId(aid),
            "package_id": ObjectId(pid),
            "section_id": ObjectId(sid),
            "viewed_card_ids": [{"$oid": "57fbd6df7d2ba5447f72c79a"}
        })
        """
        pass

import hug
import cards
import pymongo
import json
import bson

from pymongo import MongoClient
from bson import json_util, ObjectId
from datetime import datetime

def getUnviewedCards(uid:hug.types.text,aid:hug.types.text,sid:hug.types.text,):
    #uid : user_id
    #aid : application_id
    #sid : section_id
    
    #/getUnviewedCards/57f57781f807e512cdbd7325/57fbe0ee7d2ba5447f72c7d0
    
    limitval = 5
    try:
        client = MongoClient('mongodb://usr_gunde_5dk:Rrd3b7yk28rbAwZb@ds035036.mlab.com:35036/gunde5dkcom')
        db = client.gunde5dkcom
    
        UnviewdCardsInfo = json.loads(json_util.dumps({'cards': []}))
        
        result_viewed_cards = db.lpath.find({
            "application_id":ObjectId(aid),
            "user_id":ObjectId(uid),
            "section_id":ObjectId(sid)
        }, {"_id":0, "viewed_card_id":1 }).limit(1)
        if result_viewed_cards.count()>0:
            viewed_card_ids = result_viewed_cards[0]["viewed_card_id"]
            unviewed_card_ids = db.cards.find({"_id":{"$nin":viewed_card_ids}}).limit(limitval)
            UnviewdCardsInfo = json.loads(json_util.dumps({'cards': unviewed_card_ids}))
    
        client.close()
    except bson.errors.InvalidId:
        #gonderilen ID ObjectID tipinde degils
        pass
    
    return UnviewdCardsInfo
    
def getViewedCards(uid:hug.types.text,aid:hug.types.text,sid:hug.types.text):
    try:
        client = MongoClient('mongodb://usr_gunde_5dk:Rrd3b7yk28rbAwZb@ds035036.mlab.com:35036/gunde5dkcom')
        db = client.gunde5dkcom    
        
        result = db.lpath.find({
            "application_id":ObjectId(aid),
            "user_id":ObjectId(uid),
            "section_id":ObjectId(sid)            
            },{"user_id":0,"section_id":0,"application_id":0})
        return json.loads(json_util.dumps({'cards': result}))    
    except bson.errors.InvalidId:
        #gonderilen ID ObjectID tipinde degils
        pass

def getViewedCard(id:hug.types.text):
    try:
        client = MongoClient('mongodb://usr_gunde_5dk:Rrd3b7yk28rbAwZb@ds035036.mlab.com:35036/gunde5dkcom')
        db = client.gunde5dkcom    
        
        result = db.lpath.find({
            "_id":ObjectId(id)
            })
        return json.loads(json_util.dumps({'cards': result}))    
    except bson.errors.InvalidId:
        #gonderilen ID ObjectID tipinde degils
        pass
    
def insViewedCard(uid:hug.types.text,aid:hug.types.text,sid:hug.types.text,cid:hug.types.text):
    #uid : user_id
    #aid : application_id
    #sid : section_id
    #cid : card_id

    client = MongoClient('mongodb://usr_gunde_5dk:Rrd3b7yk28rbAwZb@ds035036.mlab.com:35036/gunde5dkcom')
    db = client.gunde5dkcom
    
    process_result_id = ""
        
    result_viewed_cards = db.lpath.find({
        "user_id":ObjectId(uid),
        "section_id":ObjectId(sid),
        "application_id":ObjectId(aid),
        }, {"_id":1, "viewed_card_id":1 }).limit(1)
    if result_viewed_cards.count()>0:
        #update
        mongo_updaterow_id = result_viewed_cards[0]["_id"]
        #card i ekliyoruz
        viewed_cards = result_viewed_cards[0]["viewed_card_id"]
        card_mevcut = False
        for x in viewed_cards:
            if str(x) == str(cid):
                card_mevcut = True
                break
        
        if card_mevcut == False:
            viewed_cards.append(ObjectId(cid))
        
            update_result = db.lpath.update({'_id':mongo_updaterow_id}, {"$set": {
                "user_id": ObjectId(uid),
                "application_id": ObjectId(aid),
                "section_id": ObjectId(sid),
                "viewed_card_id": viewed_cards
            }}, upsert=False)
        
        process_result_id = mongo_updaterow_id
    else:
        #insert
        inserted_id = db.lpath.insert_one({
            "user_id": ObjectId(uid),
            "application_id": ObjectId(aid),
            "section_id": ObjectId(sid),
            "viewed_card_id": [ObjectId(cid)]
        }).inserted_id
        
        process_result_id = inserted_id
        
    
    last_record_status = getViewedCard(process_result_id)    
    
    return json.loads(json_util.dumps(last_record_status))
        
    





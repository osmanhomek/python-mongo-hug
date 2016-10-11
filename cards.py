import hug
import cards
from pymongo import MongoClient
import json
from bson import json_util, ObjectId

def getCards(id: hug.types.text, pid: hug.types.text):
    #id : section_id
    #pid : user_id
    limitval = 5

    client = MongoClient('mongodb://usr_gunde_5dk:Rrd3b7yk28rbAwZb@ds035036.mlab.com:35036/gunde5dkcom')
    db = client.gunde5dkcom

    #viewed cards
    result_viewed_cards = db.lpath.find({"user_id":ObjectId(pid),"section_id":ObjectId(id)}, {"_id":0, "viewed_card_ids":1 }).limit(1)
    #kayit var-yok kontrolü
    records = result_viewed_cards[0]
    print(records)
    #elimizdeki id lerden olmayan 5 kaydı aşağıdan alacağız



    result_cards = db.cards.find({"section_id":ObjectId(id)}, {"section_id":0 } ).limit(limitval)
    #"source":1, "target":1, "additional1":1, "additional2":1, "additional3":1, "avatar":1
    list_cards = list(result_cards)

    dictCards = {}
    dictCards["cards"] = list_cards
    result = json.loads(json_util.dumps(dictCards))

    client.close()

    return result

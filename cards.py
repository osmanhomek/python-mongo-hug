import hug
import cards
from pymongo import MongoClient
import json
from bson import json_util, ObjectId

def getCards(id: hug.types.text, pid: hug.types.text):
    #id : section_id
    #pid : user_id
    limitval = 3

    client = MongoClient('mongodb://usr_gunde_5dk:Rrd3b7yk28rbAwZb@ds035036.mlab.com:35036/gunde5dkcom')
    db = client.gunde5dkcom

    #viewed cards
    result_viewed_cards = db.lpath.find({"user_id":ObjectId(pid),"section_id":ObjectId(id)}, {"_id":0, "viewed_card_ids":1 }).limit(1)
    #kayit var-yok kontrolü eklenecek
    records = result_viewed_cards[0]
    viewed_card_ids = records["viewed_card_ids"]
    print(viewed_card_ids)
    print(viewed_card_ids[0])

    #tum kayitlar
    result_cards = db.cards.find({"section_id":ObjectId(id)}, {"section_id":0 } )
    for card in result_cards:
        print(card)

    result_cards = db.cards.find({"section_id":ObjectId(id),"viewed_card_ids":ObjectId(viewed_card_ids[0])}, {"section_id":0 } ).limit(limitval)
    list_cards = list(result_cards)

    dictCards = {}
    dictCards["cards"] = list_cards
    result = json.loads(json_util.dumps(dictCards))

    client.close()

    return result

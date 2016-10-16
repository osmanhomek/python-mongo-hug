import hug
import sections
from pymongo import MongoClient
import json
from bson import json_util, ObjectId

def getSections(id: hug.types.uuid):
    client = MongoClient('mongodb://usr_gunde_5dk:Rrd3b7yk28rbAwZb@ds035036.mlab.com:35036/gunde5dkcom')
    db = client.gunde5dkcom

    result = db.packages.find_one({"application_id":ObjectId(id)})
    #select * from packages where application_id = ID

    packages_sections = result["sections"]


    listSections = []
    for section_id in packages_sections:
        dict_sections = db.sections.find({"_id":section_id})
        list_section = list(dict_sections)
        listSections.append(list_section[0])

    dictSections = {}
    dictSections["sections"] = listSections
    result = json.loads(json_util.dumps(dictSections))

    client.close()

    return result

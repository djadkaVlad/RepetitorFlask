import json
from pprint import pprint

from data import goals, teachers

with open('database.json', 'w') as datajson:
    goals = json.dumps(goals, ensure_ascii=False, indent=4)
    teachers = json.dumps(teachers[0], ensure_ascii=False, indent=4)
    datajson.write(goals)
    datajson.write(teachers)

with open('database.json') as database:
    print(json.load(database))

# with open('database.json','w') as databa:


#
# with open('database.json', 'w') as datajson:
#     # datajson.write(json.dumps(content,ensure_ascii=False))
#
#     cont = json.dumps(content, ensure_ascii=False, indent=4)
#     newcont = cont.replace("'\ ", '')
#     datajson.write(newcont)

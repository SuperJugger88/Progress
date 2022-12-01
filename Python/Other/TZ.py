items = [
    {"id": 1, "parent": "root"},
    {"id": 2, "parent": 1, "type": "test"},
    {"id": 3, "parent": 1, "type": "test"},
    {"id": 4, "parent": 2, "type": "test"},
    {"id": 5, "parent": 2, "type": "test"},
    {"id": 6, "parent": 2, "type": "test"},
    {"id": 7, "parent": 4, "type": None},
    {"id": 8, "parent": 4, "type": None}
]

class TreeStore:
    def __init__(self,items) -> None:
        self.items = items

    def getAll(self):
        return items

    def getItem(self,id):
        return items[id-1]

    def getChildren(self,id):
        return [i for i in items if i["parent"] == id]

    def getAllParents(self,id):
        if items[id-1]['parent'] != 'root':
            return [(i,self.getAllParents(id=i['id'])) for i in items if i['id'] == items[id-1]['parent']]
        else:
            return []

ts = TreeStore(items)
# print(ts.getAll(),end='\n')
# print(ts.getItem(3),end='\n')
print(ts.getChildren(4),end='\n')
# print(ts.getAllParents(7),end='\n')
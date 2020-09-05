class Backpack(object):
    def __init__(self):
        self.storage = []
    def addItem(self, item):
        self.storage.append(item)
        print(item + " added to backpack")
    def contains(self):
        for x in self.storage:
            print(x)
    def removeItem(self, item):
        for x in self.storage:
            if x == item:
                self.storage.remove(x)
                print(item + " removed from backpack")
    def removeAll(self):
        self.storage.clear()
        print("All items removed")

def backpackContains(backpack):
    numberOfItems = len(backpack.storage)
    if numberOfItems > 0:
        print("Backpack contains", numberOfItems, "items:"); backpack.contains()
    else :
        print("Backpack is empty")


backpack = Backpack()
print("New backpack added")
backpackContains(backpack)
backpack.addItem("spoon")
backpack.addItem("fork")
backpackContains(backpack)
backpack.removeItem("spoon")
backpackContains(backpack)
backpack.removeAll()
backpackContains(backpack)



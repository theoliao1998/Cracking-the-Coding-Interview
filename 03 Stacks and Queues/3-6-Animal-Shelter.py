# Animal Shelter: An animal shelter, which holds only dogs and cats, operates on a strictly"first in, first
# out" basis. People must adopt either the "oldest" (based on arrival time) of all animals at the shelter,
# or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of
# that type). They cannot select which specific animal they would like. Create the data structures to
# maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog,
# and dequeueCat. You may use the built-in Linkedlist data structure.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def append(self, x):
        n = self
        while n.next:
            n = n.next
        n.next = x

class AnimalShelter:
    def __init__(self):
        self.first = None
        self.firstType = {"dog": None, "cat": None}
    
    def enqueue(self,animal):
        tmp = ListNode(animal)
        if self.first:
            self.first.append(tmp)
        else:
            self.first = tmp
        if not self.firstType[animal["type"]]:
            self.firstType[animal["type"]] = tmp

        

    def dequeueAny(self):
        if self.first.val["type"] == "dog":
            return self.dequeueDog()
        else:
            return self.dequeueCat()

    def dequeueDog(self):
        if not self.firstType["dog"]:
            return None
        t = self.firstType["dog"].next
        while t is not None and t.val["type"] != "dog":
            t = t.next
        res = self.firstType["dog"]
        self.firstType["dog"] = t
        return res.val

    def dequeueCat(self):
        if not self.firstType["cat"]:
            return None
        t = self.firstType["cat"].next
        while t is not None and t.val["type"] != "cat":
            t = t.next
        res = self.firstType["cat"]
        self.firstType["cat"] = t
        return res.val

# s = AnimalShelter()
# s.enqueue({"name":"o","type":"dog"})
# s.enqueue({"name":"a","type":"cat"})
# s.enqueue({"name":"c","type":"cat"})
# s.enqueue({"name":"d","type":"dog"})
# s.enqueue({"name":"e","type":"cat"})
# s.enqueue({"name":"t","type":"dog"})

# print(s.dequeueCat())
# print(s.dequeueAny())
# print(s.dequeueDog())
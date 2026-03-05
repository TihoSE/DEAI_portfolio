# =================Klasse===============
# Parent class
class LinkedList:
    # This is used 
    def toString(self):
        return ""
    
    def addFirst(self, value):
        return LinkedListPopulated(value, self)
    
    def remove(self):
        return ""
    
    def smallest(self):
        return ""

#  Child klasse
class LinkedListPopulated(LinkedList):

     def __init__(self, value, head):
        self.value = value
        self.head = head         


     def toString(self):
        # This print what's put inside the data
        return str(self.value)  + " " + self.head.toString()

     def addFirst(self, value):
        return LinkedListPopulated(value, self)

     def remove(self, value):
        if self.value == value:
        # eerste voorkomen gevonden, sla deze node over
            return self.head
        else:
        # behoud deze node en roep remove aan op de rest
            new_head = self.head.remove(value)
            return LinkedListPopulated(self.value, new_head)
    
     def smallest(self):
     # Als de rest leeg is, ben ik de kleinste
        if isinstance(self.head, LinkedListEmpty):
            return self.value
        else:
        # recursief kleinste van de rest
            min_rest = self.head.smallest()
            return min(self.value, min_rest)
    
    
     
#  Child klasse
class LinkedListEmpty(LinkedList):
    
    def toString(self):
        return ""

    def addFirst(self):
        return ""
    
    def remove(self):
         return ""
    
    def smallest(self):
        raise ValueError("Empty list has no smallest value")


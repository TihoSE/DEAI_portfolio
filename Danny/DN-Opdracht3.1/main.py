from LinkedList import LinkedList, LinkedListEmpty, LinkedListPopulated

empty_list = LinkedListEmpty()
the_list = LinkedListPopulated(12, empty_list)
parent_list = LinkedList()

# ====To string====
twelve = the_list.toString()
print(twelve)

# ====AddFirst====
parent_result = parent_list.addFirst(5)
print(parent_result)

# ====Remove=====
list = LinkedListPopulated(5, LinkedListPopulated(4, LinkedListPopulated(7, LinkedListPopulated(4, LinkedListEmpty()))))
print("Origineel:", list.toString())

# Verwijderd de eerste 4
list2 = list.remove(4)
print("Eerste keer verwijderd:", list2.toString())

# Verwijderd de tweede 4
list3 = list2.remove(4)
print("Tweede keer verwijderd:", list3.toString())

# === smallest ===
print(list) 
print(f"Kleinste getal: {list.smallest()}")
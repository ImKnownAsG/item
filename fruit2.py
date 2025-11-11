from item import Item

class Stand:
    def withItem(self, value):
        self = self
        #print("with: " + value )

fruit = Item("apple")
fruit.append("banana")
fruit.append("peach")
fruit = fruit.last()
fruit.insertBefore("mango")
fruit.insertAfter("pineapple")
fruit.prepend("acai")

fruit.clear()

for x in fruit:
    print(x)

myList = ['grape', 'tangerine', 'melon']

fruit.fromList(myList)

print(f'fruit after adding myList:')
for x in fruit:
    print(x)



    


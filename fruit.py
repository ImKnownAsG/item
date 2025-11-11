from item import Item

class Stand:
    def withItem(self, value):
        print("with: " + value )

fruit = Item("apple")
print(f'fruit.object(): {fruit.object()}')
fruit.append("banana")
print(f'fruit.after(): {fruit.after().object()}')
fruit.append("peach")
fruit = fruit.last()
print(f'fruit.before(): {fruit.before().object()}')
fruit.insertBefore("mango")
fruit.insertAfter("pineapple")
fruit.prepend("acai")

print(f'count before extract: {fruit.count()}')
for x in fruit:
    print(x)

fruit.extract()

print(f'count after extract: {fruit.count()}')
for x in fruit:
    print(x)

stand = Stand()
fruit.forEach(stand)

print(f'fruit @ 3: {fruit.at(3).object()}')

fruit2 = Item("kiwi")

print(f'fruit has kiwi: {fruit.has('kiwi')}')
print(f'fruit has the mango: {fruit.has("mango")}')

myList = ['grape', 'tangerine', 'melon']

fruit.fromList(myList)

print(f'fruit after adding myList:')
for x in fruit:
    print(x)

fruitList = fruit.toList()

print('fruitList:')
for _ in fruitList:
    print(_)
    
fruit.clear()

for x in fruit:
    print(x)

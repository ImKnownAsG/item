from item import Item

def fact(n):
    fact = 1
    while n > 0:
        fact *= n
        n -= 1
    
    return fact
    

def swaps(n = 1): #number of permuted items
    
    c = Item()
    
    for i in range(1, fact(n) + 1):
        t = n
        while t > 0:
            fn = fact(t)
            if i % 2 == 1:
                c.append([1,2])
                break
            elif i % fn == 0:
                if t == 2:
                    c.append([1, t + 1])
                else:
                    c.append([(i // fn) % (t + 1), t + 1])
                break
            elif i % fn == 0:
                c.append([1, t + 1])
                break
            
            t -= 1

    return c

def perm(elem, swap):
    for _ in elem.first():
        print(f'elem.first(): {_}')
        
    permList = elem.first()
    i = 0
    for _ in permList:
        print(f'permList: {_}')
        
    for _ in swap:            
        permList.append(permList.swap(_))
        

elements = 6
swapList = swaps(elements)
listCount = 0
for _ in swapList:
    listCount += 1
    #print(f'swapList: {listCount}: {_}')

elementList = Item()
for _ in range(elements):
    elementList.append(_)
    
permutation = perm(elementList, swapList)
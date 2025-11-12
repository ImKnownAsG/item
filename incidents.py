from item import Item

class DayOfWeek:
    _day = Item('Mon')
    _day.append('Tue' )
    _day.append('Wed')
    _day.append('Thu')
    _day.append('Fri')
    _day.append('Sat')
    _day.append('Sun')

    def day():
        return DayOfWeek.object()

    def yesterday():
        if DayOfWeek ==  DayOfWeek.first() :
             DayOfWeek  =  DayOfWeek.last()
        else:
             DayOfWeek  =  DayOfWeek.yesterday() 
        return  day 

incident = Item()
incident.append(173) # made up data for business that averages a couple of incidents per year
incident.append(214)
incident.append(187)

for  i  in  incident :
    for  j  in range( incident.object() ):
         DayOfWeek = DayOfWeek.yesterday() 
    print(f'Event happened on { DayOfWeek.day() }')

print(f'Original incident happened on { DayOfWeek.day() }.')
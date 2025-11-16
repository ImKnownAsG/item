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
        return DayOfWeek._day.object()

    def yesterday():
        if DayOfWeek._day ==  DayOfWeek._day.first() :
             DayOfWeek._day  =  DayOfWeek._day.last()
        else:
             DayOfWeek._day  =  DayOfWeek._day.before() 
        return  DayOfWeek._day 

incident = Item()
incident.append(173) # made up data for business that averages a couple of incidents per year
incident.append(214)
incident.append(187)

totalDays = 0

#for i in incident:
#    print(f'incident: {incident}')
    
for  i  in  incident :
    print(f'Starting from day {DayOfWeek._day.object()}')
    totalDays += i
    #print(f'i: {i}')
    for  j  in range( i ):
         DayOfWeek._day = DayOfWeek.yesterday() 
    print(f'Event happened {i} days ago, on { DayOfWeek._day.object() }')

print(f'Original incident happened {totalDays} ago,  on { DayOfWeek._day.object() }.')
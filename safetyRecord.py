from item import Item

weekList = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
dayOfWeek = Item()
for _ in weekList:
    dayOfWeek.append(_)    

safetyDays = [137, 170, 109, 155, 196, 114, 163, 148, 170, 125]
safetyHistory = Item()
for _ in safetyDays:
    safetyHistory.append(_)

startDay = dayOfWeek
totalDays = 0
for rec in safetyHistory:
    j = 0
    while j < rec:
        if dayOfWeek == dayOfWeek.first():
            dayOfWeek = dayOfWeek.last()
        else:
            dayOfWeek = dayOfWeek._prev
        j += 1
        totalDays += 1

print(f'The ending day of the week is {dayOfWeek.object()}')
print(f'The days since injury history of {safetyDays} represented:')
print(f'  {totalDays} days')
print(f'which is:')
print(f'  {totalDays // 7} week(s) and {totalDays % 7} day(s)')
print(f'from the starting day {startDay.object()}.')





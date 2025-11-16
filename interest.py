from item import Item

class Rate:
    def __init__(self, apy, days):
        self._apy = apy
        self._days = days

rateHistory = Item()
rateHistory.append(Rate(4, 236))
rateHistory.append(Rate(3, 187))
rateHistory.append(Rate(7, 29))

principal = 50000.00
compound = 365

print(f'Before starting, principal is: ${principal:,.2f}')
for i in rateHistory:
    print(f'Calculating {i._apy}% interest for {i._days} days')
    for j in range(i._days):
        principal = principal * (1 + i._apy / 100 / 365)
        print(f'Principal is now: ${principal:,.2f}')


print(f'Balance: ${principal:,.2f}')

'''
Interest
APR, APY
interest = principal * 4%
interest = principal * 4 / 100
interest = principal * 4 / 100
interest = principal * 4 / 100 / (365/4)
interest = principal * 4 / 100 / (365/12)

principal = principal * (1 + (4 / 100 / (365)))
principal +=
'''
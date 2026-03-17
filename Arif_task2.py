dates={"12/3/26":10000,
       "13/3/26":30000,
       "14/3/26":20000  }     
       

total = 0

for price in dates.values():
    total += price

avg = total / len(dates)

print(avg)

#volatility days
volatility = []

for key, value in dates.items():

    if value >= avg * 1.05:
        print(key, "volatile")
    elif value <= avg * 0.95:
        print(key, "volatile")
    else:
        print(key, "normal")  


list=list(dates.items())   
print(list)     


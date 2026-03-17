list1=[" 23.5 ", "low", " 45.0","HIGH ", "30.2"]


result = []

for i in list1:
    clean = i.strip().lower()
    result.append(clean)

print(result)
   

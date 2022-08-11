#methods in dictionary
capital={"usa":"washington","india":"new delhi","russia":"moscow"}

print(capital["russia"])
print(capital.get("germany"))
print(capital.keys())            
print(capital.values())        
print(capital.items)  


capital.update({"russia":"los angelos"})
print(capital)
capital.update({"india":"mahali","usa":"moscow"})
print(capital)
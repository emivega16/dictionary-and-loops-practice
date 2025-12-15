# this is what we will use for the video intro to dictionaries = a collection of (key:value) pairs ordered and changeable. No duplictaes

capitals = {"USA": "Washington D.C.",
            "India": "New Dehli", 
            "China": "Beijing",
            "Russia": "Moscow"}

#print(dir(capitals))
#print(help(capitals))
print(capitals.get("Japan"))

if capitals.get("Russia"):
    print("That capital exists")
else:
    print("That capital doesn't exist")

capitals.update({"Germany": "Berlin"})
capitals.update({"USA": "Detroit"})
capitals.popitem()

keys = capitals.keys()

for key in capitals.keys():
    print(key)

values = capitals.values()
for value in capitals.values():
    print(value)

print(capitals)


items = capitals.items()
for key, value in capitals.items():
    print(f"{key}: {value}")

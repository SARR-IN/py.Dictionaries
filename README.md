# py.Dictionaries

#unordered,changeable and DO NOT ALLOW duplicate values

dictt={
    "name":"Ronak",
    "age":25,
    "vehicle:"Tata Safari",
    "DOB":"12-12-12"
    "fruits":["Oranges","Mango","Apple"]
}

print(dictt)
print(len(dictt))
print(type(dictt))
     
X=dictt.get("vehicle")
print(x)

dictt["vehicle"]= "Bike"

print(dictt)


dictt.update("name":"Prakash")

print(dictt)


dictt["colour"]="Black"
print(dictt)


dictt.pop("vehicle")

print(dictt)

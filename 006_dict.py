empty={}
person={
    "name":"john",
    "age":"20"
}
print(person["name"])
person2 = dict(name="Patric", age=21)
print(person2)

dict_with_2_pow = {x: 2**x for x in range(0, 11)}
print(dict_with_2_pow)

print(person["name"])
print(person.get("name"))

person['address'] = "Vinnitsia"
print(person)

for key in person:
    print(key, person[key])


for value in person.values():
    print(value)

for key, value in person.items():
    print(key, value)


d1 = {"a":1}
d1.update({"b":2, "a": 2})
d1 |= {"c":3}
print(d1)
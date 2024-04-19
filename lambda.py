people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Aime", "house": "Revenclaw"},
    {"name": "Draco", "house": "Stytherin"}
    
]



def f(person):
    return person["name"]

#Or  people.sort(key= lambda person: person["name"] )


people.sort(key=f)
print(people)
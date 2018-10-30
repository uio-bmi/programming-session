
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return "Person(%s, %s)" % (self.name, self.age)


def old(data):
    age_dict = {}
    for person in data:
        if person.age > 35:
            age_dict[person.name] = person.age
    return age_dict


def new(data):
    """ TODO """
    return {person.name: person.age for person in data if (person.age > 35)}


if __name__ == "__main__":
    data = [Person(name, age) for name, age in
            [("Knut", 30), ("Knut", 29), ("Stine", 30),
             ("Brita", 60), ("Olav", 40)]]
    print(data)
    assert old(data) == new(data)
    print("SUCSESS!")

# Family tree 

family = {}
n = int(input("Enter number of family members: "))

for i in range(n):
    name = input("\nEnter name: ")
    father = input("Enter father's name: ")
    mother = input("Enter mother's name: ")

    family[name] = {"father": father, "mother": mother}

print("\nFAMILY TREE")

for name in family:
    print(name, "-> Father:", family[name]["father"],
          "Mother:", family[name]["mother"])

person = input("\nEnter a person's name: ")
if person in family:
    father = family[person]["father"]
    mother = family[person]["mother"]

    print("\nFather:", father)
    print("Mother:", mother)

    print("Siblings:")
    for name in family:
        if name != person and (
            (family[name]["father"] == father and father != "None") or
            (family[name]["mother"] == mother and mother != "None")
        ):
            print(name)

    print("Children:")
    for name in family:
        if family[name]["father"] == person or family[name]["mother"] == person:
            print(name)

else:
    print("Person not found")

animals={
    "lion": "scary",
    "elephant":"big",
    "teddy":"soft",
}

things = animals
animals["teddy"]="new soft"
print(things)

things=animals.copy()
# this makes shallow copy where underlying change is not reflected in new
# dictionary
# with immutable objects , shallow or deep copy is same
# only if objects in dictionary are mutable then shallow vs deep is relevant


animals["teddy"] = "old soft"
print(things)


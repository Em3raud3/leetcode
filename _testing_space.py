thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

for i in thisdict:
    if i == "brand":
        thisdict["brand"] = thisdict["brand"] + "Chevy"


print(thisdict["brand"])

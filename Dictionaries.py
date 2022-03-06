# key and value pair
name_age_dict = {}
name_age_dict["Alice"] = 20
name_age_dict["Bob"]= 30
name_age_dict["carol"]=40
name_age_dict["diana"] = 50

print(name_age_dict["Bob"])
# keys, values and items
# print(name_age_dict.keys())
# print(name_age_dict.values())
# print(name_age_dict.items())

for name, age in name_age_dict.items():
    print("{}'s age is {}".format(name, age))
    



uniquota = {"subscribers": 10000,
            "views" : 50000,
            "likes" : 10001}

print(f"uniquota has {uniquota['views']} views")



print(uniquota.keys())  #keys print parameters

print(uniquota.values()) #values print the parameters values

uniquota.pop("likes")
uniquota.update({"comments":23})
print(uniquota)

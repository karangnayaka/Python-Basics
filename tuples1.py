#if data is enclosed in {} flower brackets it cannot be accessed through indices
#but we can acess data through{} by accessing directly through string variables

list1 = [1234, 3, 4, 5]
uniquota = {"subscribers": 100, "views": 50 }
print(uniquota["views"])
print("Thanks for your suppport")
print(f"Uniquota channel has {uniquota['subscribers']} subscribers and {uniquota['views']}viewrs")

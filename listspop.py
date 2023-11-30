#lists
#removwe and pop of elements in a lists
products = ["mask" , "shield" , "drink","oxygen"]

products.pop(2)
print(products)

products.remove("mask")

print(products)
#for inserting we are usinng products.insert("")
products.insert(1,"spray")
print(products)

products.insert(-1,"python")
print(products)

products.insert(len(products),"code")
print(products)
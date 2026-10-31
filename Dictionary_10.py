"""
Dictionary: order
key and value pair, {}

"""
car={} # Empty dictionary
print(type(car))

# here "brand" is known as Key and "Toyota" is value
# every pair is known as an item which is known "brand" and "Toyota"
# car1={
#     "brand": "Toyota",
#     "color": "Red",
#     "price": 8000
# }

# print(car1)
# print(type(car1))

# # to print brand
# print(car1["brand"]) # this gives "Toyota"
# print(car1.get("price"))
# print(car1.keys()) # it gives keys
# print(car1.values())
# print(car1.items())
# # change key name
# car1["brand"] = "Tesla" # we have change Toyota by Tesla
# print(car1.items())
# car1["color"] =["red", "pink"]
# print(car1.items())
# car1["model"] = 2026
# car1.update({"engine type":"electric"}) # adding or updating with new addition
# print(car1.items())
# car1.pop("price")  #remove price items
# print(car1.items())
# car1.popitem()  # remove last item
# print(car1.items())
# #car1.clear() # clear the content or dictionary
# print(car1.items())

# using loops in dictionary only keys
# for i in car1:
#     print(i)

# # using loops in dictionary only keys
# for i, j in car1.items():
#     print(i, j)

# # Nested dictionary.  One dictionary contains another dictionary

cars={
    "car2":{"brand": "Toyota",
    "color": "Red",
    "price": 8000
    },

    "car3":{"brand": "Tesla",
    "color": "Black",
    "price": 1000
    }
}
print(cars)
print(cars["car2"])
print(cars["car2"]["price"])

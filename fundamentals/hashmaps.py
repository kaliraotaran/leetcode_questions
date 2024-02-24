# its bascially a dictionary in python

# key: value , the key need to be of immutable type(single value, that means it cant be an array)

my_dict = {"name": "John", 1234567890: "john@gmail.com"}# example of how to declare

# default dicts - it automatically assigns key values to a dictionary so u don't have to 

from collections import defaultdict
city= defaultdict(list) # here the default value type will be a list (hence the parameter )
city["New York"].append("Empire State Building")
# or
cities = ["calgary", "BC", "Toronto"]
city["canada"]+= cities
# print(city)


# retriving data
# hashmap.keys() - return all the keys in the list
# hashmap.values()  - returns all the values o fthe keys in the list
# hashmaps.items() - return combination of keys as well as the values

mydict = {}
# or could use mydict = defaultdict(list)
cities = ['LA', 'LV', 'NY']
mydict['US'] = [] # initialized a key  with empty list
mydict['US'] += cities
print(mydict.items())


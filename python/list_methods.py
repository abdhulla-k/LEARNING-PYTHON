numbers = [2, 1, 5, 4, 3]

# map function
mapResult = list(map(lambda x: x * 2, numbers))
print(mapResult)

# filter function
filterResult = list(filter(lambda x: x % 2 == 0, numbers))
print(filterResult)

# reduce function
from functools import reduce
reduceResult = reduce(lambda x, y: x + y, numbers)
print(reduceResult)

# sorted() using to sort an arry. it will return a new array as sorted
sortedArray = sorted(numbers)
print(sortedArray)

my_set = {1, 2, 3}
print(my_set)

my_set = {1.0, "hello", (1, 2)}
print(my_set)

my_set2 = {1,2,3,2,4,3,5,2,1}
print(my_set2)

my_set3 = set([1, 2, 3, 2, 4, 3, 5, 2, 1])
print(my_set3)

num_set = set([0,1,3,4,5])
print("original set:")
print(num_set)
num_set.pop()
print("after removing first element:")
print(num_set, "\n")
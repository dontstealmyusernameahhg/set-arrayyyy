import array as arr

array_num = arr.array('i', [1, 2, 3, 3, 4, 4, 5])
print("Original array:", array_num)
print("number of occurrence of number 3 in the array:", array_num.count(3))

array_num.reverse()
print("Reversed array:", array_num)
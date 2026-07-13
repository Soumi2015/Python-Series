lst = ['Study', 'Coding', 'Hobbies', 'Playing', 'Eating']

print("Length of list:", len(lst))
print("First Element:", lst[0])
print("Last Element:", lst[-1])

lst.append('Stories')
print("Updated List :", lst)

lst.remove('Coding')
print("Updated List after removing Coding:", lst)

lst.sort()
print("Sorted List:", lst)

lst.pop(1)
print("Updated List :", lst)

lst.reverse()
print("Reversed List :", lst)

print("Multiplication on List :", lst*2)

lst = lst[:4]
print("Sliced List :", lst)

lst.clear()
print("Updated List :", lst)
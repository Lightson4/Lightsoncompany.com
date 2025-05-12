#creating a set
my_set = {1,2,3,4,5,}
print(my_set)
print(my_set)
#list
my_list2 = [1,2,3,4,5]
list = set([1,2,3,4,5])
print(type(list))
#basic set opperators
#adding and removing element
my_set.add(7)
print(my_set)
my_set.remove(4,)
print(my_set)
#counting unque word in set
southeast = {'abia', 'imo', 'anambra', 'delta','cross river' 'rivers'}
print(southeast)
print('lagos' in southeast)
southeast.add('enugu')
print(southeast)
print('enugu' in southeast)
#mathematical operation
itme1 = {'rice', 'beans', 'garri', 'soup', 'tomoto'}
itme2 = {'bevirages', 'whine', 'water', 'blood', 'spirit'}
itme1.add('blood')
itme2.add('beans')
union_item =itme1.union(itme2)
print(union_item)
#intersection
intersection_item = itme2.intersection(itme1)
print(intersection_item)
print(itme2)
#itme1.intersection_update(itme2)
print(itme1)
print(itme2)
print(itme2.difference(itme1))
diff_item = itme1.difference(itme2)
print(diff_item)
#symethic  difference
symethic_item = itme1.symmetric_difference(itme2)
print(symethic_item)
# Is Subset
print(itme1.issubset(itme2))
# is superset
print(itme1.issuperset(itme2))
#convanting the list of word to set
test = 'i am learing data analysis, in order to be a data analyst'
words = test.split()
unque_words = set(words)
print(test)
print(unque_words)
print(len(unque_words))


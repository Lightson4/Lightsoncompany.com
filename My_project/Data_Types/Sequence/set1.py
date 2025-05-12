art = {'music', 'fine arts', 'drama', 'dance', 'literature', 'design'}
science = {'biology', 'physis', 'chemistry', 'computer', 'mathematic', 'computer'}
#union
union_class =art.union(science)
print(union_class)
print(art)
print(science)
#difference
print(science.difference(art))
diff_class = art.difference(science)
print(diff_class)
#symmetric
symmetic_class = art.symmetric_difference(science)
print(symmetic_class)
intersection_class = science.intersection(art)
#intersection
art.add('biology')
science.add('music')
intersection_class = art.intersection(science)
print(intersection_class)
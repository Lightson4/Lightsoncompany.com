#This is a sample of tuple
'''
Potential = ([1, 2,] , [3,5,])
print(Potential[0])
print(type(Potential))
'''
# This is a sample of mixed Tuple
'''
Light = (2, 2.3, 23, "IT", True, False)
print((Light)
'''
# Accessing the elemnts
Oko = ("love lodge", "you lodge", "delight lodge", "akudinaobi lodge", "girls lodge", "grace lodge")
print(Oko[1:3])
# more on tuple
wisdom = ("where are you going?")
ble = ( "i am going to aba")
topic = wisdom + ble
print(topic)
#tuple oppression
Numbers = (1,2,3,4,5,6,7,8,9,10)
multiply= Numbers * 3
print(multiply)
#addition side
Number2 = (1,2,3,4,5,6,7,8,3,9,10,2,3,3)
addition = Numbers + Number2
print(addition)

# immutability of Tuple
list = [ 1,2,4,5,]
list[0] = 'Light'
print(list[0])
print(list)
'''
Number2[1]= 'Nelson'
print(Number2)
'''
#tuple method
print(Number2.count(3))
#packing and unpacking
pack_tuple = 33,4.5, 'it'
print(pack_tuple)
#unpack tuple
a, b, c=pack_tuple
print(a)
print(b)
print(c)
#nested tuple
school = ("anambra",("oko", "unizk", "covenant") , ("abia", ("absu", "rhyma", "abia poly")) )
print(school)

#creating dictionary
mt_dictionary = {}
print(type(mt_dictionary))
#creating dictionary with its keys and values
student = {'name': 'Nelson', 'Age': 26, 'Grade': 35}
print(student)
nelson = {'surname': 'ochor', "age": 62, 'state of origin': 'abia', 'hobbies': ['drinking', 'fighing','eating']}
print(nelson)
#accessing element in dictionary
print(nelson['hobbies'])
print(nelson['state of origin'])
#accessing dictionary using get method
print(nelson.get('surname'))
print(nelson.get('dept'))
#modifing dictionary element using add, update and delete
nelson['age'] = 63
print(nelson['age'])
nelson['department']= "Business Admin"
print(nelson)
del nelson['age']
print(nelson)
nelson['state of origin'] = 'imo'
print(nelson)
#accessing all key and valuse in dictionary
keys = nelson.keys()
print(keys)
Values = nelson.values()
print(Values)
items = nelson.items()
print(items)
#iterating over dictionary
for keys in nelson.keys():
    print(keys)
for keys in nelson.items():
    print(items)
for keys, Value in nelson.items():
    print(f"{keys}: {Value}")
#nessted dictionary
Students = {
    'Light' :{ 'School': 'Fed Poly', 'age': 98, 'Grade': 'B', 'Course':'Business Admin'},
    'Nelson' :{ 'School': 'Arete World Tech Academy', 'age': 27, 'Grade': 'C', 'Course':'Data Analysis'}
}
print(Students)
members = {
    'kings' :{'church': "mountain of fire", 'age': 632, 'position': '1st' },
    'queen' :{'church': "light of the world", 'age': 323, 'position': '2nd'},}
keys = members.keys()
print(keys)

for members, info in members.values():
    print(f'name: {members}')
    for key, value in info.items():
        print(f"{key}:{value}")
#accessing nested distionary
print(Students['Light']['age'])
print(Students['Nelson']['age'])
#iterating nested dictionary
for Student_id, Students_info in Students.items():
    print(f"{Student_id}:{Students_info}")
    for key, value in Students_info.items():
        print(f"{key}:{value}")

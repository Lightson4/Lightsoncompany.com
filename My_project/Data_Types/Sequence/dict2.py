#define the dictionary with personal dat
trainees = {
    'gift':{'age': 72, 'date of bath': '7th august', 'gender': 'male', 'nationality': 'france', 'contact number': 090688922},
    'blessing': {'age': 28, 'dfb': '29th jan, 2087', 'gender': 'female', 'nationality': 'usa', 'contact number': 090665695},
    'confy': {'age': 20, 'dfb': '7th july, 2123', 'gender': 'male', 'nationality': 'naigeria', 'contact number': 09068897988},
    'light': {'age': 22, 'dfb': '7th merch, 3242', 'gender': 'female', 'nationality': 'canada', 'contact number': 0906767679},
    'pp': {'age': 65, 'dfb': '1st nov, 2013', 'gender': 'male', 'nationality': 'niger', 'contact number': 09068232312},
    'kaka':{'age': 28, 'dfb': '9th dec, 2011', 'gender': 'female', 'nationality': 'ghana', 'contact number': 09864557554}
    }
print(trainees)

#display the trainees and their personal info
for trainees, info in trainees.items():
    print(f"name: {trainees}")
    for key, value in info.items():
        print(f"{key} : {value}")
trainees['gift'['age']] = 543
print('name: gift')
for key, value in trainees ['gift'].items():
    print(f"{key} : {value}")

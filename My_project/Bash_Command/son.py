import pandas as pd
import json
'''#convert a jsn string into a python dictionary
json_string = '{"Name": "Light", "Age": 35, "City": "ABA"}'
data = json.loads(json_string)
print(data)
'''
#assinment
Data = '''[
        {"Name":"Light", "Age": 99, "City": "ABA"},
        {"Name":"Bright", "Age": 85, "City": "OMOBA"},
        {"Name":"Nelson", "Age": 95, "City": "IMO"}
        ]'''
Data_SON = json.loads(Data)
#convert to dataframe
df = pd.DataFrame(Data_SON)
# to read to jsaon
print(df)


# Workers Date
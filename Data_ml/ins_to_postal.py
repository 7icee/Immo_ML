import pandas as pd
import json

postal_data = pd.read_excel('postal_code.xlsx')  # Replace with your actual file path


code_ins_to_postal = {}
for index, row in postal_data.iterrows():
    code_ins = row['Code INS']
    code_postal = row['Codes postaux']
    langue = row['Langue']

    if pd.notna(langue):
            code_ins_int = int(code_ins)
            
            postal_list = [postal.strip() for postal in str(code_postal).split(',') if postal.strip()]
            
            if code_ins_int in code_ins_to_postal:
                code_ins_to_postal[code_ins_int].extend(postal_list)
            else:
                code_ins_to_postal[code_ins_int] = postal_list
print(code_ins_to_postal)


with open('ins_to_postal.json', 'w') as json_file:
    json.dump(code_ins_to_postal, json_file)
import pandas as pd
import json


property_data = pd.read_csv('pre_dataset.csv')
postal_data = pd.read_excel('postal_data.xlsx')
postal_data_dict = postal_data.set_index('Code INS')[['Population', 'Wealth Index']].to_dict(orient='index')


with open('ins_to_postal.json', 'r') as json_file:
    ins_to_postal = json.load(json_file)


def get_ins_code(postal_code):
    for ins_code, postal_list in ins_to_postal.items():
        if str(int(postal_code)) in postal_list:
            return int(ins_code) 
    return None

def get_population(ins_code):
    if ins_code in postal_data_dict:
        return postal_data_dict[ins_code]['Population']
    return None

def get_wealth_index(ins_code):
    if ins_code in postal_data_dict:
        return postal_data_dict[ins_code]['Wealth Index']
    return None


property_data['INS Code'] = property_data['postal_code'].apply(get_ins_code)
property_data['Population'] = property_data['INS Code'].apply(get_population)
property_data['Wealth Index'] = property_data['INS Code'].apply(get_wealth_index)

property_data.to_csv('dataset_with_ins_code.csv', index=False)

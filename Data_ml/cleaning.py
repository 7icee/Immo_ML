import pandas as pd
import numpy as np


class DataCleaning:

    def __init__(self, filepath: str):
        self.filepath = filepath
        self.data = pd.read_csv(filepath)

    def drop_irrelevant(self):
        irrelevant_columns = ['house_index', 'url', 'property_subtype','locality', 'street', 'number', 'box', 'furnished', 'fireplace', 'fireplaceCount','landSurface','province','typeOfSale']
        self.data = self.data.drop(columns=[col for col in irrelevant_columns if col in self.data.columns])
    
    def fill_empty_with_zero(self, column_name: str):
        self.data[column_name] = self.data[column_name].fillna(0)

    def drop_rows_with_empty(self, column_name: str):
        self.data = self.data.dropna(subset=[column_name])
        
    def fill_with_mode(self, column_name: str):
        mean_value = self.data[column_name].mode()[0]
        self.data[column_name] = self.data[column_name].fillna(mean_value)
    
    def process_building_state(self):
        self.data['buildingState'] = self.data['buildingState'].fillna('UNKNOWN')
        self.data['buildingState'] = self.data['buildingState'].map({
            'GOOD': 1,
            'AS_NEW': 2,
            'TO_RENOVATE': 3,
            'TO_BE_DONE_UP': 4,
            'JUST_RENOVATED': 5,
            'TO_RESTORE': 6,
            'UNKNOWN': 0
        })
    
    def process_property_type(self):
        self.data['property_type'] = self.data['property_type'].map({
            'HOUSE': 0,
            'APARTMENT': 1
        })
    
    def convert_numbers_to_int(self):
        numeric_cols = self.data.select_dtypes(include=[np.number]).columns
        self.data[numeric_cols] = self.data[numeric_cols].astype(int)
        

    def process(self):
        self.drop_irrelevant()

        columns_to_fill = ['gardenSurface', 'terraceSurface', 'surfaceOfThePlot']
        for column in columns_to_fill:
            if column in self.data.columns:
                self.fill_empty_with_zero(column)

        rows_to_drop = ['livingArea', 'INS Code', 'Population', 'Wealth Index', 'price']
        for column in rows_to_drop:
            if column in self.data.columns:
                self.drop_rows_with_empty(column)
        
        self.fill_with_mode("facades")
        self.process_building_state()
        self.process_property_type()
        self.convert_numbers_to_int()

        return self.data


if __name__ == "__main__":

    dataset_path = "dataset.csv"
    cleaner = DataCleaning(dataset_path)

    processed_data = cleaner.process()
    processed_data.to_csv("processed_dataset.csv", index=False)
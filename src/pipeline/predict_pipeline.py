import os
import sys
sys.path.append('D:/WORK/Personnel/Python projects/Projects/used-car-price')
import pandas as pd
from src.exception import CustomException
from src.utils import load_object
from src.logger import logging

class PredictionPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        
        try:
            model_path = os.path.join("artifacts\model.pkl")
            processor_path = os.path.join("artifacts\preprocessor.pkl")

            model = load_object(file_path = model_path)
            preprocessor = load_object(file_path = processor_path)

            data_scale = preprocessor.transform(features)
            prediction = model.predict(data_scale)

            return prediction
        
        except Exception as e:
            logging.info(CustomException(e, sys))
            raise CustomException(e, sys)

class CustomData:
    def __init__(self,
                Location: str, Year: int,
                Kilometers_Driven: int, Fuel_Type : str,
                Transmission: str, Owner_Type: str,
                Mileage_kmpl : float, Engine_CC : float,
                Power_bhp : float, Seats : float):
        
        self.Location = Location
        self.Year = Year
        self.Kilometers_Driven = Kilometers_Driven
        self.Fuel_Type = Fuel_Type
        self.Transmission = Transmission
        self.Owner_Type = Owner_Type
        self.Mileage_kmpl = Mileage_kmpl
        self.Engine_CC = Engine_CC
        self.Power_bhp = Power_bhp 
        self.Seats = Seats

    def get_data_as_dataframe(self):
        try:
            custom_data_input = {
                "Location" : [self.Location],
                "Year" : [self.Year],
                "Kilometers_Driven" : [self.Kilometers_Driven],
                "Fuel_Type" : [self.Fuel_Type],
                "Transmission" : [self.Transmission],
                "Owner_Type" : [self.Owner_Type],
                "Mileage_kmpl" : [self.Mileage_kmpl], 
                "Engine_CC" : [self.Engine_CC],
                "Power_bhp" : [self.Power_bhp], 
                "Seats" : [self.Seats]
            } 
        
            return pd.DataFrame(custom_data_input)
        
        except Exception as e:
            logging.info(CustomException(e, sys))
            raise CustomException(e, sys)
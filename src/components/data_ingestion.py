import os
import sys
sys.path.append('D:/WORK/Personnel/Python projects/Projects/used-car-price')
from src.exception import CustomException
from src.logger import logging
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransfromation
from src.components.data_transformation import DataTransfromationConfig

from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer

from src.utils import load_data_from_S3

@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join("artifacts", "train.csv")
    test_data_path: str=os.path.join("artifacts", "test.csv")
    raw_data_path: str=os.path.join("artifacts", "data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):

        logging.info("Entered the data ingestion method or component")

        # Read data
        try:
            # # Read local Data
            # df = pd.read_csv(r"notebook\used_car_price.csv")
            # df.drop(columns=[df.columns[0], "Name", "New_Price"], axis=1, inplace=True)
            # df["Mileage"] = [float(str(i).split(" ")[0]) for i in  df["Mileage"].values]
            # df["Engine"] = [float(str(i).split(" ")[0]) for i in  df["Engine"].values]
            # df["Power"] = [float(str(i).split(" ")[0]) for i in  df["Power"].values]

            # Read data from S3
            dic = {'Name':[], 'Location':[], 'Year':[], 'Kilometers_Driven':[], 'Fuel_Type':[], 'Transmission':[],
            'Owner_Type':[], 'Mileage':[], 'Engine':[], 'Power':[], 'Seats':[], 'New_Price':[], 'Price':[]}
            
            df = load_data_from_S3(service_name = 's3', region_name= 'eu-west-3', aws_access_key_id = 'AKIA2DZSO5WT2YESOTPW', aws_secret_access_key = "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", Bucket = "mlprojects-dataset", Key = "used-car-price-dataset/used_car_price.csv", dic = dic)
            df["Year"] = pd.to_numeric(df["Year"], errors='coerce').astype('Int64')
            df["Kilometers_Driven"] = pd.to_numeric(df["Kilometers_Driven"], errors='coerce').astype('Int64')

            Mileage = []
            for i in  df["Mileage"].values:
                if len(str(i).split(" ")[0])>1:
                    Mileage.append(float(str(i).split(" ")[0]))
                else:
                    Mileage.append(np.nan)
            df["Mileage"] = Mileage

            Engine = []
            for i in  df["Engine"].values:
                if len(str(i).split(" ")[0])>1:
                    Engine.append(float(str(i).split(" ")[0]))
                else:
                    Engine.append(np.nan)
            df["Engine"] = Engine

            Power = []
            for i in  df["Power"].values:
                if len(str(i).split(" ")[0])>1:
                    Power.append(float(str(i).split(" ")[0]))
                else:
                    Power.append(np.nan)
            df["Power"] = Power
            Seats = []
            for i in  df["Seats"].values:
                if len(str(i))>1:
                    Seats.append(float(str(i)))
                else:
                    Seats.append(np.nan)
            df["Seats"] = Seats


            df = df.rename(columns={'Mileage': 'Mileage_kmpl', 'Engine': 'Engine_CC', 'Power': 'Power_bhp'})
            
            logging.info("Read the dataset as dataframe")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info("Train test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.25, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Ingestion of the data is completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            logging.info(CustomException(e,sys))
            raise CustomException(e,sys)

if __name__ == "__main__":
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()

    data_transformation = DataTransfromation()
    train_arr_, test_arr_, _ = data_transformation.initiate_data_transfromation(train_data, test_data)

    model_trainer = ModelTrainer()
    print(model_trainer.initiate_model_trainer(train_arr_, test_arr_))
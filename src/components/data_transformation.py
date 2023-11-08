import os
import sys
sys.path.append('D:/WORK/Personnel/Python projects/Projects/used-car-price')
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


from src.exception import CustomException
from src.logger import logging

from src.utils import save_object

@dataclass
class DataTransfromationConfig:
    preprocessor_obj_file_path = os.path.join("artifacts", "preprocessor.pkl")

class DataTransfromation:
    def __init__(self):
        self.data_transformation_config = DataTransfromationConfig()

    def get_data_transfromer_object(self):
        
        try:
            numerical_features = ['Year', 'Kilometers_Driven', 'Mileage_kmpl', 'Engine_CC', 'Power_bhp', 'Seats']
            categorical_features = ['Location', 'Fuel_Type', 'Transmission', 'Owner_Type']

            num_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="mean")),
                    ("scaler", StandardScaler())
                ]
            )

            cat_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="most_frequent")),
                    ("encoder", OneHotEncoder())
                ]
            )

            logging.info(f"Numerical features : {numerical_features}")
            logging.info(f"Categorical features : {categorical_features}")

            preprocessor = ColumnTransformer(
                [
                    ("num_pipeline",num_pipeline, numerical_features),
                    ("cat_pipeline",cat_pipeline, categorical_features)
                ]
            )

            return preprocessor

        except Exception as e:
            logging.info(CustomException(e, sys))
            raise CustomException(e, sys)
        
    
    def initiate_data_transfromation(self, train_path, test_path):
        
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("Read train and test data completed")

            logging.info("Obtaining preprocessing object")

            preprocessing_obj = self.get_data_transfromer_object()

            target_column_name = "Price"
            # numerical_features = ['Year', 'Kilometers_Driven', 'Mileage (kmpl)', 'Engine (CC)', 'Power (bhp)', 'Seats']

            input_feature_train_df = train_df.drop([target_column_name], axis=1)
            target_train_df = train_df[target_column_name]

            input_feature_test_df = test_df.drop([target_column_name], axis=1)
            target_test_df = test_df[target_column_name]

            logging.info("Applying preprocessing object on training and testing dataframe")

            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessing_obj.fit_transform(input_feature_test_df)

            train_arr = np.c_[input_feature_train_arr, np.array(target_train_df)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_test_df)]

            logging.info("Saved preprocessing object")

            save_object(
                file_path = self.data_transformation_config.preprocessor_obj_file_path,
                obj = preprocessing_obj
            )

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path
            )

        except Exception as e:
            logging.info(CustomException(e, sys))
            raise CustomException(e, sys)
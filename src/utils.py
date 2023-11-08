import os
import sys
sys.path.append('D:/WORK/Personnel/Python projects/Projects/used-car-price')
import pandas as pd
import numpy as np

from src.exception import CustomException
from src.logger import logging

import dill
from sklearn.metrics import r2_score
from sklearn.model_selection import RandomizedSearchCV

import boto3
import csv


def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        logging.info(CustomException(e, sys))
        raise CustomException(e, sys)
    
def evaluate_model(x_train, y_train, x_test, y_test, models, params):

    try:
        report = {}
        for i in range(len(list(models))):
            model = list(models.values())[i]
            param = list(params.values())[i]

            clf = RandomizedSearchCV(model, param, n_iter = 5, random_state=42)
            clf.fit(x_train, y_train)

            model.set_params(**clf.best_params_)
            model.fit(x_train, y_train)

            y_predict = model.predict(x_test)
            
            score = r2_score(y_test, y_predict)

            report[list(models.keys())[i]] = score

        return report
    
    except Exception as e:
        logging.info(CustomException(e, sys))
        raise CustomException(e, sys)


def load_object(file_path):
    try:
        with open(file_path, 'rb') as file_obj:
            return dill.load(file_obj)
        
    except Exception as e:
        logging.info(CustomException(e, sys))
        raise CustomException(e, sys)
    


def load_data_from_S3(service_name, region_name, aws_access_key_id, aws_secret_access_key, Bucket, Key, dic):
    
    try:
        # Connexion to S3
        s3 = boto3.client(
        service_name = service_name,
        region_name = region_name,
        aws_access_key_id = aws_access_key_id,
        aws_secret_access_key = aws_secret_access_key
        )

        obj = s3.get_object(Bucket=Bucket, Key=Key)    
        data = obj['Body'].read().decode('utf-8').splitlines()
        records = csv.reader(data)

        headers = next(records)[1:] #5

        for record in records:
            elements = list(record)[1:]
            for i in range(len(elements)):
                dic[list(dic.keys())[i]].append(elements[i])
    except Exception as e:
        logging.info(CustomException(e, sys))
        raise CustomException(e, sys)
    
    df = pd.DataFrame(dic)

    return df
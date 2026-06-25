import joblib
import numpy as np
import pandas as pd
from pathlib import Path
    
class PredictionPipeline:
    def __init__(self):
        self.model = joblib.load('artifacts/model_trainer/model.joblib')
        self.encoder = joblib.load('artifacts/data_transformation/encoder.joblib')

    def predict(self, data: pd.DataFrame):
        if 'customer_id' in data.columns:
                data = data.drop(columns=['customer_id'])

        categorical_cols = ['country', 'gender']
        encoded_array = self.encoder.transform(data[categorical_cols])

        encoded_cols = self.encoder.get_feature_names_out(categorical_cols)
        encoded_df = pd.DataFrame(encoded_array, columns=encoded_cols, index=data.index)

        final_df = pd.concat([data.drop(columns=categorical_cols), encoded_df], axis=1)

        prediction = self.model.predict(final_df)
        return prediction
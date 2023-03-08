!pip3 install -r requirements.txt

import mlflow
import mlflow.spark
import pandas as pd
from pyspark.sql import SparkSession

logged_model = '/home/cdsw/.experiments/b97v-6z85-mp1g-bsfl/ny3t-o1jj-6di5-mve0/artifacts/sparkml-model'

# Load model as a PyFuncModel.
loaded_model = mlflow.pyfunc.load_model(logged_model)

a = 0
b = "spark"

data = {"id": [a], "text": [b]}
        
df = pd.DataFrame(data)


# Predict on a Pandas DataFrame.
loaded_model.predict(df)
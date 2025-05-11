import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline,make_pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import Normalizer,StandardScaler, OneHotEncoder,MinMaxScaler,LabelEncoder
# Step 1: Data Preparation
students_df = pd.read_csv('./part4/students.csv')
numeric_features = ['Age', 'GPA']
categorical_features = ['Major']
# Step 2: Define Transformation Pipelines
numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', MinMaxScaler())
    ])
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', LabelEncoder())
    ])
#Step 3: Create & Execute the Full Transformer
preprocessor = ColumnTransformer(
transformers=[ 
              ('nos', numeric_transformer, numeric_features),
              ('cats', categorical_transformer, categorical_features)
              ],remainder='passthrough') # or remainder='drop' to drop remaining column or keep

transformed_features = preprocessor.fit_transform(students_df)
transformed_students_df = pd.DataFrame(
transformed_features, 
columns=preprocessor.get_feature_names_out()
)
#transformed_students_df.rename({"nos__Age":"Age"},inplace=True)
transformed_students_df.columns=['Age', 'GPA', 'Major_ SE',
                                 'Major_CS','Major_DS',
                                 'Major_DSS', 'Major_IS',
                                 'Id','Name',
                                 'Year']
print(transformed_students_df.iloc[:,[7,8,9,0,1,2,3,4,5,6]])
print(transformed_students_df.loc[:,['Id','Name','Year','Age', 'GPA', 'Major_ SE',
                                 'Major_CS','Major_DS',
                                 'Major_DSS', 'Major_IS',
                                 ]])
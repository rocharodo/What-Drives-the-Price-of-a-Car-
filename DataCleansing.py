import pandas as pd
import numpy as np
from sklearn.preprocessing import OrdinalEncoder, StandardScaler, OneHotEncoder, FunctionTransformer, LabelEncoder
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import warnings
warnings.filterwarnings('ignore')

# The following script was created to do the data cleansing and data preparation so it can be saved in a csv file and doesn't need
# to be loaded every time there is a change in the model or somewhere in the process.


my_time = datetime.datetime.now().time()
print("Start:", my_time.strftime("%H:%M"))

df = pd.read_csv('data/vehicles.csv')

# Remove id and VIN features
df = df.drop_duplicates(subset=['manufacturer','model','year','price'], keep='last')
#df = df.query("VIN.notnull()").drop_duplicates(subset=['VIN'])

df = df.drop(['id', 'VIN','size',"region"], axis=1)
#df = df.drop(["paint_color"],axis = 1)
# Remove outliers in the price column
q_low = df["price"].quantile(0.1)
q_hi  = df["price"].quantile(.95)

df = df[(df["price"] < q_hi) & (df["price"] > q_low)]

df = df[df['year'].notna()]
df = df[df['manufacturer'].notna()]

#condition NaN 0.437 filling the NaN values with a new category called "unknown" or "missing".

df.dropna(subset=['odometer','transmission','manufacturer'], inplace=True)

#df.dropna(subset=['model'], inplace=True)

df['model'] = df['model'].str.replace("'","").str.replace('"','').str.replace("&","").str.replace("$","").str.replace("♿","").str.replace("$","").str.replace("(","").str.replace("/","").str.replace("%","").replace("*","")

#df['model'] = df['model'].str.replace("'","-").str.replace('"','-')

df['fuel'].fillna('gas', inplace=True)
df['title_status'].fillna('missing', inplace=True)
df['drive'].fillna('unknown', inplace=True)
df['paint_color'].fillna('unknown', inplace=True)
df['condition'].fillna('unknown', inplace=True)
df['type'].fillna('unknown', inplace=True)

ordinal_encoder = OrdinalEncoder()
#df['condition_encoded'] = ordinal_encoder.fit_transform(df[['condition']])

my_time = datetime.datetime.now().time()

print("1:", my_time.strftime("%H:%M"))

#filling the NaN values with "6 cylinders", which is the second most frequent value (0.284)

bridge_df = pd.DataFrame(df, columns=['manufacturer'])
enc_df = pd.get_dummies(bridge_df, columns=['manufacturer'],dtype='int')
df = df.join(enc_df)

bridge_df = pd.DataFrame(df, columns=['transmission'])
enc_df = pd.get_dummies(bridge_df, columns=['transmission'],dtype='int')
df = df.join(enc_df)

bridge_df = pd.DataFrame(df, columns=['paint_color'])
enc_df = pd.get_dummies(bridge_df, columns=['paint_color'],dtype='int')
df = df.join(enc_df)

bridge_df = pd.DataFrame(df, columns=['state'])
enc_df = pd.get_dummies(bridge_df, columns=['state'],dtype='int')
df = df.join(enc_df)

bridge_df = pd.DataFrame(df, columns=['fuel'])
enc_df = pd.get_dummies(bridge_df, columns=['fuel'],dtype='int')
df = df.join(enc_df)

#df['title_status_encoded'] = le.fit_transform(df['title_status'])
#df['drive_encoded'] = le.fit_transform(df['drive'])
#df['type_encoded'] = le.fit_transform(df['type'])

bridge_df = pd.DataFrame(df, columns=['title_status'])
enc_df = pd.get_dummies(bridge_df, columns=['title_status'],dtype='int')
df = df.join(enc_df)

bridge_df = pd.DataFrame(df, columns=['drive'])
enc_df = pd.get_dummies(bridge_df, columns=['drive'],dtype='int')
df = df.join(enc_df)

bridge_df = pd.DataFrame(df, columns=['type'])
enc_df = pd.get_dummies(bridge_df, columns=['type'],dtype='int')
df = df.join(enc_df)

bridge_df = pd.DataFrame(df, columns=['condition'])
enc_df = pd.get_dummies(bridge_df, columns=['condition'],dtype='int')
df = df.join(enc_df)


my_time = datetime.datetime.now().time()

print("Before model:", my_time.strftime("%H:%M"))

#bridge_df = pd.DataFrame(df, columns=['model'])
#enc_df = pd.get_dummies(bridge_df, columns=['model'],dtype='int')
#df = df.join(enc_df)

my_time = datetime.datetime.now().time()

print("After model:", my_time.strftime("%H:%M"))

man_cnt = 1000
def GetModels():
    manufacturer_models = pd.DataFrame()
    for manufacturer in np.sort(df['manufacturer'].unique().astype("str")):
        # Get the unique models for this manufacturer
        models = df[df['manufacturer'] == manufacturer]['model'].unique()
        
        mod_cnt = 1
        for model in np.sort(models.astype("str")):
            manufacturer_model = pd.DataFrame({"manufacturer": [manufacturer],
                                               "model": [model],
                                              "man_id":[man_cnt],
                                              "model_id":[mod_cnt]})
            manufacturer_models = pd.concat([manufacturer_models, manufacturer_model], ignore_index=True)
            mod_cnt += 1
        man_cnt += 1000
    return manufacturer_models

#manufacturer_models = GetModels()

def create_unique_id(row):
    manu_model = manufacturer_models.query(f'manufacturer =="{row["manufacturer"]}"')
    manufacturer = row["manufacturer"]    
    manufacturer_id = manu_model.man_id.values
    model = row["model"]
    try:
        if pd.notnull(row['model']) and row['model'] != '':
            model_id = manufacturer_models.query(f"manufacturer == '{manufacturer}' and model =='{model}'")["model_id"]
            return manufacturer + "_" + model_id.values[0].astype(str)
        else:
            return manufacturer
    except Exception as e:
        print(f'caught {type(e)}: e')      
        print("An exception occurred:",{row["manufacturer"]}," model:",model)

#This line has been removed so it doesn't call the function that splits manufacturers and models
#df['manufacturer_model'] = df.apply(create_unique_id, axis=1)

#bridge_df = pd.DataFrame(df, columns=['manufacturer_model'])
#enc_df = pd.get_dummies(bridge_df, columns=['model'],dtype='int')
#df = df.join(enc_df)


df.to_csv("data/car_man_model2.csv")
my_time = datetime.datetime.now().time()

print("Finished:", my_time.strftime("%H:%M"))

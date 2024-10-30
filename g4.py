from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import make_column_transformer
from sklearn.feature_selection import RFE, SequentialFeatureSelector
from sklearn.linear_model import Ridge, Lasso, ElasticNet
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression
from joblib import Parallel, delayed
import numpy as np
import pandas as pd
import datetime

import warnings
warnings.filterwarnings('ignore')

def cleanse_data(df):
    df = df.drop_duplicates(subset=['VIN','manufacturer','model','price','year'], keep='last')
    
    df = df.drop(['id', 'VIN','size',"region"], axis=1)
    # Remove outliers in the price column
    q_low = df["price"].quantile(0.1)
    q_hi  = df["price"].quantile(.95)
    
    df = df[(df["price"] < q_hi) & (df["price"] > q_low)]
    
    df.dropna(subset=['year'], inplace=True)
    df.dropna(subset=['manufacturer'], inplace=True)
    
    #condition NaN 0.437 filling the NaN values with a new category called "unknown" or "missing".
    
    df.dropna(subset=['odometer','transmission','state'], inplace=True)
    
#    df.dropna(subset=['model'], inplace=True)
    
    df['model'] = df['model'].str.replace("'","").str.replace('"','').str.replace("&","").str.replace("$","").str.replace("♿","").str.replace("$","").str.replace("(","").str.replace("/","").str.replace("%","").replace("*","")
    
    df['model'] = df['model'].str.replace("'","_").str.replace('"','_')
    
    df.fillna({"fuel":'gas'}, inplace=True)
    df.fillna({"title_status":'missing'}, inplace=True)
    df.fillna({"drive":'unknown'}, inplace=True)
    df.fillna({"paint_color":'other'}, inplace=True)
    df.fillna({"condition":'unknown'}, inplace=True)
    df.fillna({"type":'missing'}, inplace=True)
    df.fillna({"cylinders":'unknown'}, inplace=True)
    df.fillna({"model":'unknown'}, inplace=True)
    df['manufacturer_model'] = df['manufacturer'] + '_' + df['model']
    df = df.drop(['manufacturer', 'model'], axis=1)
    
    return df


# Load data
df = pd.read_csv('data/vehicles.csv')

# Remove id and VIN features
df = cleanse_data(df)

# Split data
X = df.drop('price', axis=1)
y = df['price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define preprocessing transformer
categorical_columns = X.select_dtypes(include=['object']).columns
numerical_columns = X.select_dtypes(include=['int32','int64','float64']).columns

# Define transformers for numerical and categorical columns
numerical_transformer = Pipeline([
    ('scaler', StandardScaler(with_mean=True, with_std=True)),
#    ('pca', PCA(n_components=2))  # adjust component count
])

filled_values = [
    df[column].unique() for column in categorical_columns
]

categorical_transformer = Pipeline([
    ('onehot', OneHotEncoder(
        handle_unknown='ignore', 
        sparse_output=True,
    )),
])



# Update column transformer
transformer = make_column_transformer(
    (categorical_transformer, categorical_columns),
    (numerical_transformer, numerical_columns),
    remainder='drop'
)



# Define models and parameters
models = {
    "ridge": {
        "model": Ridge(),
        "selector": "",
        "params": {
            "ridge__alpha": [0.1, 1.0, 10.0]
        }
    },
    "lasso": {
        "model": Lasso(warm_start=True, max_iter=5000),
        "selector": "",
        "params": {
            "lasso__alpha": [0.1, 1.0, 10.0]
        }
    },
    "elastic_net": {
        "model": ElasticNet(warm_start=True),
        "selector": "",
        "params": {
            "elastic_net__alpha": [0.1, 1.0, 10.0],
            "elastic_net__l1_ratio": [0.2, 0.5, 0.8]
        }
    },
    'linear':{
        "model": LinearRegression(),
        "selector": "",
        "params": {
            "linear__fit_intercept": [True, False]
        }
    },
    
#    "rfe": {
#        "model": Ridge(),
#        "selector": RFE(Lasso(), n_features_to_select=4),
#        "params": {
#            "rfe__alpha": [0.1, 1.0, 10.0]
#        }
#    },
#    "sfs": {
#        "model": Ridge(),
#        "selector": SequentialFeatureSelector(Lasso(), n_features_to_select=4),
#        "params": {
#            "sfs__alpha": [0.1, 1.0, 10.0]
#        }
#    },
}

model_time = {}
# Parallelize model training
def train_model(name, config, X_train, y_train):
    print(name)
    start_time = datetime.datetime.now().time()
    print("Start:", start_time.strftime("%H:%M"))
    
    if config["selector"] == "":
        pipeline = Pipeline(steps=[('preprocessor', transformer), (name, config['model'])])
    else:
        pipeline = Pipeline(steps=[('preprocessor', transformer), ("selector",config["selector"]), (name, config['model'])])

    grid = GridSearchCV(pipeline, param_grid=config['params'], cv=5, n_jobs=-1, verbose=2)
#    print(grid)
    grid.fit(X_train, y_train)
    end_time = datetime.datetime.now().time()
    print(name)
    print("End:", end_time.strftime("%H:%M"))
    model_time[name] = {"start_time": start_time, "end_time":end_time}
    return grid, model_time


results = Parallel(n_jobs=-1)(delayed(train_model)(name, config, X_train, y_train) for name, config in models.items())

# Evaluate models

for (name, config), (grid, model_time) in zip(models.items(), results):
    print(f"Model: {name}")
    print(f"Best Parameters: {grid.best_params_}")
    print(f"Start Time: {model_time[name]["start_time"]}")
    print(f"End Time: {model_time[name]["end_time"]}")
    print(f"Best Score: {grid.best_score_}")
#    grid = results[i]
    y_pred = grid.predict(X_test)
    score = grid.score(X_test, y_test)
    print(f'Score: {score}')
    print(f"MAE: {mean_absolute_error(y_test, y_pred)}")
    print(f"MSE: {mean_squared_error(y_test, y_pred)}")
    print(f"R2 Score: {r2_score(y_test, y_pred)}")
    print("------------------------")

    

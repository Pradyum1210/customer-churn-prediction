from ast import Or
import random

from regex import P
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler, StandardScaler , OneHotEncoder

def model(data):
    data.drop(["customerID"],axis = 1 , inplace = True)
    x = data.drop(["Churn"],axis = 1)
    y = data["Churn"]
    cat_columns = []
    num_columns = []
    for cols in x:
        if data[cols].dtype == "str":
            cat_columns.append(cols)
        elif data[cols].dtype in ["float64","int64"]:
            num_columns.append(cols)
    

    # Transformer
    transform = ColumnTransformer(transformers=[
        ("cat",OneHotEncoder(sparse_output=False , drop="first"),cat_columns),
        ("num",StandardScaler(),num_columns)
    ]
    )
    
    # Logistic Regression pipeline
    lr_pipeline = Pipeline(steps=[
        ("preprocessing",transform),
        ("model" , LogisticRegression(class_weight = "balanced"))
    ]   
    )

    # Random Forest pipeline
    rf_pipeline = Pipeline(steps=[
        ("preprocessing" , transform),
        ("model" , RandomForestClassifier(n_estimators=100,random_state=42))
    ]
    )

    # Data split
    x_train , x_test , y_train , y_test = train_test_split(x,y , random_state=42 , test_size=0.3)


    # Training 
    lr_pipeline.fit(x_train , y_train)

    rf_pipeline.fit(x_train , y_train)

    # Testing
    y_pred_lr = lr_pipeline.predict(x_test)

    y_pred_rf = rf_pipeline.predict(x_test)

    
    # Classification Report 

    print("\nLogistic Regression: \n")
    print(classification_report(y_test , y_pred_lr))

    print("\nRandom Forest: \n")
    print(classification_report(y_test , y_pred_rf))
    


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
churn = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv',na_values='?')
churn.isna().sum()
categorical_attr = [var for var in churn.columns if churn[var].dtypes =='object']
numerical_attr = [var for var in churn.columns if churn[var].dtypes == 'int64' or 'float64']
churn['gender'].replace(['Male','Female'],[0,1],inplace=True)
churn['Partner'].replace(['Yes','No'],[1,0],inplace=True)
churn['Dependents'].replace(['Yes','No'],[1,0],inplace=True)
churn['PhoneService'].replace(['Yes','No'],[1,0],inplace=True)
churn['MultipleLines'].replace(['No phone service','No','Yes'],[0,1,2],inplace=True)
churn['InternetService'].replace(['DSL','No','Fiber optic'],[1,0,2],inplace=True)
churn['OnlineBackup'].replace(['No internet service','No','Yes'],[0,1,2],inplace=True)
churn['OnlineSecurity'].replace(['No internet service','No','Yes'],[0,1,2],inplace=True)
churn['DeviceProtection'].replace(['No internet service','No','Yes'],[0,1,2],inplace=True)
churn['TechSupport'].replace(['No internet service','No','Yes'],[0,1,2],inplace=True)
churn['StreamingTV'].replace(['No internet service','No','Yes'],[0,1,2],inplace=True)
churn['StreamingMovies'].replace(['No internet service','No','Yes'],[0,1,2],inplace=True)
churn['Contract'].replace(['Two year','One year','Month-to-month'],[2,1,0],inplace=True)
churn['PaperlessBilling'].replace(['Yes','No'],[1,0],inplace=True)
churn['PaymentMethod'].replace(['Credit card (automatic)','Mailed check','Electronic check','Bank transfer (automatic)'],[0,1,2,3],inplace=True)
churn['Churn'].replace(['Yes','No'],[1,0],inplace=True)
churn['MonthlyCharges'] = churn['MonthlyCharges'].astype('int64')
churn['TotalCharges'] = pd.to_numeric(churn['TotalCharges'],errors='coerce')
corr = churn.corr(method='pearson')
threshold = 0.1
a = abs(corr)
a = a[a>0.1]
a.fillna('0',inplace=True)
a.head()
relevant_features = [a.columns]
final_data = churn[['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure',
        'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity',
        'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV',
        'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod',
        'MonthlyCharges', 'TotalCharges', 'Churn']]
from sklearn.model_selection import train_test_split
X = final_data.drop(['Churn'],axis=1)
Y = final_data['Churn']
xtrain,xtest,ytrain,ytest = train_test_split(X,Y,test_size=0.3,random_state=1234)
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(strategy='median')
X_train_imputed = imputer.fit_transform(xtrain)
X_test_imputed = imputer.transform(xtest)
from sklearn.ensemble import RandomForestClassifier
rdclf = RandomForestClassifier(criterion='gini',min_samples_split=2,max_depth=12,max_features='sqrt')
rdclf.fit(X_train_imputed,ytrain)
predict_train = rdclf.predict(X_train_imputed)
predict_test = rdclf.predict(X_test_imputed)
from sklearn.metrics import classification_report
print(classification_report(ytrain,predict_train))
print('\n')
print(classification_report(ytest,predict_test))

import pickle
pickle.dump(rdclf,open('model1.pkl','wb'))
print(predict_test)

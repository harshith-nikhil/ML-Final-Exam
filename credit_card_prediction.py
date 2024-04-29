


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns




import warnings 
warnings.filterwarnings('ignore') 




df=pd.read_csv('credit_card.csv')
print(df.head())





from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier




df.drop('user_name', axis=1, inplace=True)
le = LabelEncoder()
df['occupation'] = le.fit_transform(df['occupation'])
df['marital_status'] = le.fit_transform(df['marital_status'])
df['card_given'] = le.fit_transform(df['card_given'])




X = df.drop('card_given', axis=1)
y = df['card_given']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)




scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)




models = {
    'Logistic Regression': LogisticRegression(random_state=42),
    'Random Forest': RandomForestClassifier(random_state=42),
    'Support Vector Machine': SVC(random_state=42),
    'Decision Tree': DecisionTreeClassifier(random_state=42),
    'K-Nearest Neighbors': KNeighborsClassifier()
}





for name, model in models.items():
    model.fit(X_train_scaled, y_train)
    
    y_pred = model.predict(X_test_scaled)
    
    print(f'Classification Report for {name}:')
    print(classification_report(y_test, y_pred))
    cm = confusion_matrix(y_test, y_pred)
    
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Greens', cbar=False)
    plt.title(f'Confusion Matrix for {name}')
    plt.xlabel('Predicted labels')
    plt.ylabel('True labels')
    # plt.xticks([0.5, 1.5], ['No', 'Yes'])
    # plt.yticks([0.5, 1.5], ['Yes', 'No'], rotation=0)
    plt.show()







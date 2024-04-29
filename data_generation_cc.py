import pandas as pd
import numpy as np

np.random.seed(42)


n=35

data = {
    'user_name': [f'User {i}' for i in range(1, n + 1)],
    'age': np.random.randint(18, 65, size=n),
    'income': np.random.randint(30000, 150000, size=n),
    'credit_score': np.random.randint(300, 850, size=n),
    'occupation': np.random.choice(['Engineer', 'Doctor', 'Artist', 'Teacher', 'Manager', 'Clerk', 'Trader', 'Student'], size=n),
    'marital_status': np.random.choice(['Single', 'Married', 'Divorced'], size=n),
    'card_given': np.random.choice(['Yes', 'No'], size=n, p=[0.6, 0.4]) 
}

df=pd.DataFrame(data)

print(df)


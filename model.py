import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle
from sklearn.linear_model import LinearRegression

df = pd.read_csv('data.csv',header=0)


X = df[['loan ','deposit','number_of_branch']]
y = df[['value']]

regressor = LinearRegression()
regressor.fit(X,y)
print(X.shape)

pickle.dump(regressor,open('model.pkl','wb'))

model = pickle.load(open('model.pkl','rb'))
sample = np.array([100,200,5]).reshape(1,-1)
print(model.predict(sample))

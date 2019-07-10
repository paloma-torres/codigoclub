#import
import matplotlib.pyplot as plt #para hacer graficas
import numpy as np #para preparar mis datos

#importing from scikit-learn, librerias de ML
from sklearn import datasets, linear_model

#Load dataset 
house_price=[245,321,308,199,219,405,324,319,255]
size=[1400,1600,1700,1875,1100,1550,2350,2450,1425,1700]

print(len(house_price))
print(len(size))

#reshape the input to your regression
size2=no.array(size).reshape((-1,1))

print(size2)

regr=linear_model.LinearRegression()
regr.fit(size2, house_price)
print('Coeficients:{0}'.format(regr.coef_))
print('intercept:{0}'.format(regr.intercept_))

#Formula obteined for thw trained model
def graph(formula,X_range):
   x=np.array(x_range)
   y=eval(formula)
   plt.plot(x,y)

#PLotting the prediction line
graph('regr.coef_*x + regr.intercept_', range(500,300))
plt.scatter(size,house_price,color='black')
plt.ylabel('house price')
plt.xlabel('size of house')

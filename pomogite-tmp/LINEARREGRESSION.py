import numpy as np
import pandas as pd # to import data
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#import data Advertising.csv
data = pd.read_csv('Advertising.csv', index_col=0)
data.head() # see what the data look like

#create reg lin objet
modeleReg=LinearRegression()

#create y et X
list_var=data.columns.drop("Sales")
y=data.Sales # Sales: variable dépendante y 
X=data[list_var] # toutes les autres variables: variables indépendantes 

modeleReg.fit(X,y)

print(modeleReg.intercept_)
print(modeleReg.coef_)

#calcul of R²
modeleReg.score(X,y)

# Root Mean Square Error (RMSE)
RMSE=np.sqrt(((y-modeleReg.predict(X))**2).sum()/len(y))

# les valeurs de y en fonction des valeurs prédites avec le modèle de régresssion linéaire
plt.plot(y, modeleReg.predict(X),'.')
plt.show()

# les valeurs de Y en fonction des résidus
plt.plot(y, y-modeleReg.predict(X),'.')
plt.show()
import pandas as pd
import numpy as np
from sklearn import linear_model, datasets
from sklearn import preprocessing # Min-Max Standardzation


data_source = "https://archive.ics.uci.edu/ml/machine-learning-databases/cmc/cmc.data"

names = ["Wife's age", "Wife's education", "Husband's education", "Number of children ever born", "Wife's religion",
"Wife's now working?", "Husband's occupation", "Standard-of-living index", "Media exposure", "Contraceptive method used"]

dataframe = pd.read_csv(data_source, names=names)

for column in range(0,10):
    if column not in [0,3]:
        dataframe[names[column]] = dataframe[names[column]].astype("category")

y_data = np.reshape(dataframe.pop("Contraceptive method used").values,(-1.1))
x_data = dataframe

x_data = pd.get_dummies(x_data).values
#y_data = pd.get_dummies(y_data).values

min_max_scaler = preprocessing.MinMaxScaler()
x_data= min_max_scaler.fit_transform(x_data)

idx=np.random.randint(y_data.shape[0], size=int(y_data.shape[0]))

training_idx = idx[:int(y_data.shape[0] * 0.8)]
test_idx = idx[int(y_data.shape[0] * 0.8):]

x_training, x_test = x_data[training_idx], x_data[test_idx]
y_training, y_test = y_data[training_idx], y_data[test_idx]



logreg = linear_model.LogisticRegression(multi_class='multinomial', fit_intercept=True, solver="lbfgs")

logreg.fit(x_training, y_training)

print(sum(logreg.predict(x_test) == y_test.ravel()) / len(y_test))
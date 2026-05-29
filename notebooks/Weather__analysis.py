import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
df =pd.read_csv("data/Weather__data__.csv")
numeric_df=df[[
     "temperature",
        "humidity",
        "wind_speed",
        "soil_temperature"
]]
corr_matrix = numeric_df.corr()
print(corr_matrix)
X =df[[
        "humidity",
        "wind_speed",
        "soil_temperature"
]]
Y = df["temperature"]
print(X.head())
print()
print(Y.head())
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)
print("Shape of X_train:",X_train.shape)
print("Shape of X_test:",X_test.shape)
print("Shape of Y_train:",Y_train.shape)
print("Shape of Y_test:",Y_test.shape)
model = LinearRegression()
model.fit(X_train, Y_train)
print("Model Trained Successfully!")
print("Intercept:", model.intercept_)
print("Coefficients:", model.coef_)
y_pred=model.predict(X_test)
print(y_pred)
y_pred = model.predict(X_test)
comparison = pd.DataFrame({
    "Actual": Y_test,
    "Predicted": y_pred
})
print(comparison.head(10))
mae = mean_absolute_error(Y_test, y_pred)

print("MAE:", mae)

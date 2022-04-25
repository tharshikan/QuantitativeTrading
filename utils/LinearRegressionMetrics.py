from matplotlib import pyplot as plt
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
import numpy as np
import seaborn as sns
import plotly.express as px


def linear_reg_metrics(y_test, y_pred,):
    print("Linear Regression Metrics")
    print("Mean Absolute Error:", mean_absolute_error(y_test, y_pred))
    print("Root Mean Squared Error:", np.sqrt(mean_squared_error(y_test, y_pred)))
    print("Coefficient of Determination:",r2_score(y_test, y_pred))
    print('end')
    px.scatter(y=[y_test, y_pred],  labels=["Actual", "Predicted"])
    plt.show()
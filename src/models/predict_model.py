
from sklearn.metrics import mean_absolute_error


# Function to predict and evaluate
def predict_evaluate_model(dtmodel, x_test, y_test):
    
    
    # Predict the price on the testing set
    y_pred = dtmodel.predict(x_test)
    
    # Calculate Mean Absolute Error (MAE)
    test_mae = mean_absolute_error(y_test, y_pred)

    return test_mae


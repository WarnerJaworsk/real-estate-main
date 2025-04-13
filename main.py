# from setuptools import find_packages, setup


# setup(
#     name='src',
#     packages=find_packages(),
#     version='0.1.0',
#     description='Property Price Calculator',
#     author='Warner Jaworski',
#     license='',
# )

from src.data.make_dataset import load_and_preprocess_data
from src.visualization.visualize import plot_tree
from src.features.build_features import create_dummy_vars
from src.models.train_model import train_model
from src.models.predict_model import predict_evaluate_model
import pickle


if __name__ == "__main__":
    
    # Load and preprocess the data
    df = load_and_preprocess_data('data/raw/final.csv')

    # Create dummy variables and separate features and target
    x, y = create_dummy_vars(df)

    # Train the Random Forest regression model
    dtmodel, x_test, y_test = train_model(x, y)
    
    # Predict and Evaluate the model
    test_mae = predict_evaluate_model(dtmodel, x_test, y_test)
    print(f"Test Mean Absolute Error: {test_mae}")

    # Plot visualizations
    plot_tree(dtmodel, feature_names=x.columns)
    
    # load the pickled model and make a new prediction
    with open('models/RE_Model.pkl', 'rb') as file:
        RE_Model = pickle.load(file)
        
    # Use the loaded pickled model to make predictions
    prediction = RE_Model.predict([[2012, 216, 74, 1 , 1, 618, 2000, 600, 1, 0, 0, 6, 0, 0]])
    print(f"Prediction for the input data: {prediction}")
  

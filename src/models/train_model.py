from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
import pickle


# Function to train the model
def train_model(x, y):
    # Splitting the data into training and testing sets
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=567)

    
    # Train the decsion tree model
    dt = DecisionTreeRegressor(max_depth=5, max_features=10, random_state=567)
    dtmodel = dt.fit(x_train,y_train)

    
    # Save the trained model
    with open('models/RE_Model.pkl', 'wb') as file:
        pickle.dump(dtmodel, file)
    

    return dtmodel, x_test, y_test



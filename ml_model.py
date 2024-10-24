from sklearn.linear_model import LinearRegression

# Dummy dataset for simplicity
X = [[1, 2], [2, 3], [3, 4], [4, 5]]
y = [5, 7, 9, 11]

# Train the model
model = LinearRegression()
model.fit(X, y)

def suggest_title(user_input1, user_input2):
    """Predict a title score based on two user inputs."""
    predicted_score = model.predict([[user_input1, user_input2]])[0]
    return f"Predicted title score: {predicted_score}"


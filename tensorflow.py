import tensorflow as tf
import numpy as np

true_slope = 8.0
true_intercept = 12.0
X = np.linspace(0, 15, 200)  
y = true_slope * X + true_intercept + np.random.normal(0, 3, size=X.shape)

# Build a simple linear regression model (y = wx + b)
model = tf.keras.Sequential([
    tf.keras.layers.Dense(1, input_shape=(1,))
])

# Compile with optimizer and loss function
model.compile(optimizer='adam', loss='mse')


model.fit(X, y, epochs=100, verbose=0)

weights, bias = model.layers[0].get_weights()

print(f"True slope: {true_slope:.2f}, True intercept: {true_intercept:.2f}")
print(f"Model learned slope: {weights[0][0]:.2f}, Model learned intercept: {bias[0]:.2f}")

# Test the model with a new input
x_test = np.array([[20.0]])
y_pred = model.predict(x_test, verbose=0)

print(f"Prediction → For x = {x_test[0][0]}, y ≈ {y_pred[0][0]:.2f}")

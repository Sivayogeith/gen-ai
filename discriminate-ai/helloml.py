import questionary
import tensorflow as tf
import numpy as np
from tensorflow import keras
import os

model_filename = "model.keras"
epochs = 80
# y=5x+1 is the relationship between each x and its corresponding y in the array
x = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0], dtype=float)
y = np.array([-4.0, 1.0, 6.0, 11.0, 16.0, 21.0, 26.0, 31.0], dtype=float)

def train():
    print("Training the model...")
    model = tf.keras.Sequential([keras.layers.Dense(1, input_shape=[1])]) # one layer ANN

    # compile the model with optimizer sgd = stochastic gradient descent, mse = mean squared error
    model.compile(optimizer='sgd', loss='mse')

    print("Running Epochs...")
    model.fit(x, y, epochs=epochs)
    model.save(model_filename)
    return model

def load_model():
    return keras.models.load_model(model_filename)

if os.path.exists(model_filename):
    model = load_model()
else:
    model = train()

x = float(questionary.text("Enter a number to predict:").ask())
print(f"Predicting for number: {x}")

print("Model: " + str(model.predict([x])[0]))  # predicting the result
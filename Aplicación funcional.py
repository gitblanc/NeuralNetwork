import tensorflow as tf
import numpy as np


def selectOption():
    correct = False
    num = 0
    while not correct:
        try:
            num = int(input("------number: "))
            correct = True
        except ValueError:
            print("Error, enter an integer")
    return num


def introduceTemp():
    correct = False
    num = 0
    while not correct:
        try:
            num = int(input("------Temperature to convert: "))
            correct = True
        except ValueError:
            print("Error, enter a valid temperature")
    return num


def introduceDistance():
    correct = False
    num = 0
    while not correct:
        try:
            num = int(input("------Distance to convert: "))
            if num >= 0:
                correct = True
        except ValueError:
            print("Error, enter a valid temperature")
    return num


def celsiusToFahrenheit():
    celsiusRequested = introduceTemp()
    celsius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
    fahrenheit = np.array([-40, 14, 32, 46.4, 59, 71.6, 100.4], dtype=float)

    oculta1 = tf.keras.layers.Dense(units=3, input_shape=[1])
    oculta2 = tf.keras.layers.Dense(units=3)
    salida = tf.keras.layers.Dense(units=1)
    modelo = tf.keras.Sequential([oculta1, oculta2, salida])

    modelo.compile(
        optimizer=tf.keras.optimizers.Adam(0.1),
        loss='mean_squared_error'
    )

    historial = modelo.fit(celsius, fahrenheit, epochs=1000, verbose=False)
    resultado = modelo.predict([celsiusRequested])
    print("Result: " + str(resultado) + " Fahrenheit.")


def fahrenheitToCelsius():
    fahrenheitRequested = introduceTemp()
    celsius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
    fahrenheit = np.array([-40, 14, 32, 46.4, 59, 71.6, 100.4], dtype=float)

    oculta1 = tf.keras.layers.Dense(units=3, input_shape=[1])
    oculta2 = tf.keras.layers.Dense(units=3)
    salida = tf.keras.layers.Dense(units=1)
    modelo = tf.keras.Sequential([oculta1, oculta2, salida])

    modelo.compile(
        optimizer=tf.keras.optimizers.Adam(0.1),
        loss='mean_squared_error'
    )

    historial = modelo.fit(fahrenheit, celsius, epochs=1000, verbose=False)
    resultado = modelo.predict([fahrenheitRequested])
    print("Result: " + str(resultado) + " Celsius.")


def kmToMiles():
    kmRequested = introduceDistance()

    km = np.array([1, 70, 0, 32, 987, 22, 100], dtype=float)
    miles = np.array([0.621371, 43.496, 0, 19.8839, 613.293, 13.6702, 62.1371], dtype=float)

    oculta1 = tf.keras.layers.Dense(units=3, input_shape=[1])
    oculta2 = tf.keras.layers.Dense(units=3)
    salida = tf.keras.layers.Dense(units=1)
    modelo = tf.keras.Sequential([oculta1, oculta2, salida])

    modelo.compile(
        optimizer=tf.keras.optimizers.Adam(0.1),
        loss='mean_squared_error'
    )

    historial = modelo.fit(km, miles, epochs=1000, verbose=False)
    resultado = modelo.predict([kmRequested])
    print("Result: " + str(resultado) + " miles")


left = False
option = 0

while not left:
    print("---------Operations available---------")
    print("1. Convert Celsius to Fahrenheit")
    print("2. Convert Fahrenheit to Celsius")
    print("3. Convert km to miles")
    print("0. EXIT")

    option = selectOption()
    if option == 1:
        celsiusToFahrenheit()
    elif option == 2:
        fahrenheitToCelsius()
    elif option == 3:
        kmToMiles()
    elif option == 0:
        left = True
    else:
        print("\nPlease introduce a valid option...\n")

print("Finishing...")

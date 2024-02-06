import tensorflow as tf

print(f"Wersja TensorFlow: {tf.__version__}")

#ładowanie zbioru danych
mnist = tf.keras.datasets.mnist
(x_train,y_train),(x_test,y_test) = mnist.load_data()

#normalizacja danych
x_train,x_test = x_train/255.0, x_test/255.0

print(x_train.shape)
print(x_test.shape)

#model sieci neuronowej
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28,28)),
    tf.keras.layers.Dense(128,activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10)
])

predictions = model(x_train[:1]).numpy()
print(predictions)

print("__________________________________________")
#funkcja softmax zwraca prawdopodobieństwa dla każdego elementu zwanego logit (rezprezentacja każdej cyfry 0-9)
print(tf.nn.softmax(predictions).numpy())

loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
print(loss_fn(y_train[:1],predictions).numpy())

#kompilacja modelu
model.compile(optimizer='adam',
              loss=loss_fn,
              metrics=['accuracy'])

model.fit(x_train,y_train,epochs=5)

#ocena modelu
print(model.evaluate(x_test,y_test,verbose=2))

#predykacja obraz
probability_model = tf.keras.Sequential([
    model,
    tf.keras.layers.Softmax()
])

print(probability_model(x_test[:5]))

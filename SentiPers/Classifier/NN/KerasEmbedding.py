from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers import Embedding
from keras.layers.convolutional import Conv1D
from keras.layers.convolutional import MaxPooling1D
from SentiPers.WordEmbedding import KerasWE
from keras.utils.np_utils import to_categorical
from keras.metrics import categorical_accuracy

# Get data and sizes from Keras Word Embedding
x_train, x_test, y_train, y_test = KerasWE.get_data()
vocab_size, max_length = KerasWE.get_sizes()

categorical_y_train = to_categorical(y_train, 5)
categorical_y_test = to_categorical(y_test, 5)

# Define a CNN model
# It must be changed (We have 5 value instead of just negative or positive)
model = Sequential()
model.add(Embedding(vocab_size, 100, input_length=max_length))
model.add(Conv1D(filters=32, kernel_size=8, activation='relu'))
model.add(MaxPooling1D(pool_size=2))
model.add(Flatten())
model.add(Dense(10, activation='relu'))
model.add(Dense(5, activation='sigmoid'))
print(model.summary())

# compile network
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=[categorical_accuracy])
# fit network
model.fit(x_train, categorical_y_train, epochs=10, verbose=2)

# evaluate
loss, acc = model.evaluate(x_test, categorical_y_test, verbose=0)
print('Test Accuracy: %f' % (acc*100))

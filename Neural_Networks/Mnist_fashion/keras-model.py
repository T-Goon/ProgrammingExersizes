import time
start = time.time()

from tensorflow import keras
import tensorflow as tf

# load the mnist fashion dataset
data = keras.datasets.fashion_mnist
(x_train, y_train), (x_test, y_test) = data.load_data()

# pixel values are 0-255, so scale the data
x_train = x_train / 255.0
x_test = x_test / 255.0

batch_size = 128
num_epoch = 20
num_classes = 10

# reshape the inputs to a 4D array
x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)
x_test = x_test.reshape(x_test.shape[0], 28,  28, 1)

# convert the labels to one-hot vectors
y_train_onehot = keras.utils.to_categorical(y_train, num_classes)
y_test_onehot = keras.utils.to_categorical(y_test, num_classes)

train_dataset = tf.data.Dataset.from_tensor_slices((x_train, y_train_onehot)
).batch(batch_size).shuffle(60000).repeat()
test_dataset = tf.data.Dataset.from_tensor_slices((x_test, y_test_onehot)
).batch(batch_size).shuffle(10000).repeat()

# layer weight initializers
weight_init = keras.initializers.VarianceScaling(scale=1, mode="fan_avg",
distribution="truncated_normal")
weight_initRelu = keras.initializers.VarianceScaling(scale=2, mode='fan_in',
distribution='truncated_normal')

# initialize the model
model = keras.Sequential()
model.add(keras.layers.Conv2D(filters=32, kernel_size=(4,4), activation='relu',
    input_shape = (28, 28, 1), kernel_initializer=weight_initRelu))
model.add(keras.layers.MaxPool2D(pool_size=2))

model.add(keras.layers.Conv2D(filters=64, kernel_size=(4,4), activation='relu',
kernel_initializer=weight_initRelu))
model.add(keras.layers.MaxPool2D(pool_size=2))

model.add(keras.layers.Flatten())
model.add(keras.layers.Dense(800, activation='sigmoid',
kernel_initializer=weight_init))
model.add(keras.layers.Dense(num_classes, activation='softmax'))

model.compile(optimizer = keras.optimizers.Adam(),
    loss = 'categorical_crossentropy', metrics = ['accuracy'])

# make a callback to record accuracy
class AccHistory(keras.callbacks.Callback):
    def on_train_begin(self, logs={}):
        self.acc = []

    def on_epoch_end(self, batch, logs={}):
        self.acc.append(logs.get('acc'))

his = AccHistory()

# train the model
model.fit(train_dataset, epochs=num_epoch, steps_per_epoch=500,
    callbacks=[his], validation_data=test_dataset, validation_steps=5)

# evaluate the model
score  = model.evaluate(test_dataset, steps = 80)

# print out evaluation results
print('Test Loss: ', score[0])
print('Test Accuracy: ', score[1])

end = time.time()
print('Time: ',end - start)

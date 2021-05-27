# Timothy Goon
# LSTM to predict the IMDB_reviews data set

from tensorflow import keras
from keras.backend.tensorflow_backend import set_session
from tensorflow.keras.callbacks import ModelCheckpoint
import tensorflow as tf
import numpy as np
import os
import string
import re

config = tf.compat.v1.ConfigProto()
config.gpu_options.allow_growth = True
config.log_device_placement = True
sess = tf.compat.v1.Session(config=config)
set_session(sess)

# path to data set files
data_path_train_pos = "aclImdb/train/pos/"
data_path_train_neg = "aclImdb/train/neg/"
data_path_test_pos = "aclImdb/test/pos/"
data_path_test_neg = "aclImdb/test/neg/"
vocab_path = "aclImdb/imdb.vocab"

batch_size = 50
rev_size = 500

def main():
    # create dict from provided vocab file so that each word has a unique id
    vocab_size = 10000
    vocab = build_vocab(vocab_path, vocab_size)

    # create lists of all of the data files
    data_train_pos = os.listdir(data_path_train_pos)
    data_train_neg = os.listdir(data_path_train_neg)
    data_test_pos = os.listdir(data_path_test_pos)
    data_test_neg = os.listdir(data_path_test_neg)
    # combine lists
    data_train_files = data_train_pos + data_train_neg
    data_test_files = data_test_pos + data_test_neg

    # extract the text from each file
    data_train_pos = [read_words(data_path_train_pos, x) for x in data_train_pos]
    data_train_neg = [read_words(data_path_train_neg, x) for x in data_train_neg]
    data_test_pos = [read_words(data_path_test_pos, x) for x in data_test_pos]
    data_test_neg = [read_words(data_path_test_neg, x) for x in data_test_neg]

    # combine the text
    data_train = data_train_pos + data_train_neg
    data_test = data_test_pos + data_test_neg

    # remove puncutaion that is not contained in the vocab
    for i in range(len(data_train)):
         data_train[i] = [s for s in data_train[i] if s not in ['\"', '.',',']]
         data_test[i] = [s for s in data_test[i] if s not in ['\"', '.',',']]

    # convert all the words to lower case
    for i in range(len(data_train)):
         data_train[i] = [s.lower() for s in data_train[i]]
         data_test[i] = [s.lower() for s in data_test[i]]

    # save memory space
    del data_train_pos
    del data_train_neg
    del data_test_pos
    del data_test_neg

    # convert the words to their respective id numbers
    data_train = to_id(data_train, vocab)
    data_test = to_id(data_test, vocab)

    # create validation set inputs
    data_test = data_test[:int(len(data_test)/2)]
    data_valid = data_test[int(len(data_test)/2):]

    # pad and truncate text sequences
    data_train = keras.preprocessing.sequence.pad_sequences(data_train, maxlen=rev_size, padding='post', truncating='post',value=0)
    data_test = keras.preprocessing.sequence.pad_sequences(data_test, maxlen=rev_size, padding='post', truncating='post',value=0)
    data_valid = keras.preprocessing.sequence.pad_sequences(data_valid, maxlen=rev_size, padding='post', truncating='post',value=0)

    reversed_vocab = dict(zip(vocab.values(), vocab.keys()))

    # get the rating of each review from the filename
    rating_list_train = [x[x.find('_')+1:x.find('.')] for x in data_train_files]
    rating_list_test = [x[x.find('_')+1:x.find('.')] for x in data_test_files]

    del data_train_files
    del data_test_files

    # convert from string to int
    rating_list_train = [int(x) for x in rating_list_train]
    rating_list_test = [int(x) for x in rating_list_test]


    # convert to one-hot vector
    # rating_list_train  = [x-1 for x in rating_list_train]
    # rating_list_test  = [x-1 for x in rating_list_test]
    # rating_list_train = keras.utils.to_categorical(rating_list_train, num_classes=10)
    # rating_list_test = keras.utils.to_categorical(rating_list_test, num_classes=10)

    # change rating from 1-10 to good vs bad
    rating_list_train = [[0] if x < 5 else [1] for x in rating_list_train]
    rating_list_test = [[0] if x < 5 else [1] for x in rating_list_test]

    # create validation set labels
    rating_list_test = rating_list_test[:int(len(rating_list_test)/2)]
    rating_list_valid = rating_list_test[int(len(rating_list_test)/2):]

    # shuffle the data
    train_pairs = np.array([[data_train[i], rating_list_train[i]] for i in range(len(data_train))])
    test_pairs = np.array(list(zip(data_test, rating_list_test)))
    valid_pairs = np.array(list(zip(data_valid, rating_list_valid)))
    np.random.shuffle(train_pairs)
    np.random.shuffle(test_pairs)
    np.random.shuffle(valid_pairs)

    rating_list_train = np.array([train_pairs[i, 1] for i in range(len(train_pairs))])
    rating_list_test = np.array([test_pairs[i, 1] for i in range(len(test_pairs))])
    rating_list_valid = np.array([valid_pairs[i, 1] for i in range(len(valid_pairs))])

    data_train = np.array([train_pairs[i, 0] for i in range(len(train_pairs))])
    data_test = np.array([test_pairs[i, 0] for i in range(len(test_pairs))])
    data_valid = np.array([valid_pairs[i, 0] for i in range(len(valid_pairs))])

    train_generator = batch_Generator(data_train, rating_list_train, batch_size)
    test_generator = batch_Generator(data_test, rating_list_test, batch_size)
    valid_generator = batch_Generator(data_valid, rating_list_valid, batch_size)

    # initialize the callback class
    hist = AccHistory()
    checkpointer = ModelCheckpoint(
    filepath="IMDB_reviews/checkpoints" + '/model2-{epoch:02d}.hdf5', verbose=1)

    model = keras.Sequential()

    model.add(keras.layers.Embedding(vocab_size, 100, input_length=rev_size))

    model.add(keras.layers.LSTM(rev_size))

    #model.add(keras.layers.Dense(50, activation='relu'))
    model.add(keras.layers.Dense(1))
    #model.add(keras.layers.Dropout(.2))
    model.add(keras.layers.Activation('relu'))

    model.compile(optimizer='Adam', loss = 'binary_crossentropy',
    metrics=['binary_accuracy'])

    model.fit_generator(train_generator.generate(), steps_per_epoch= len(data_train) // batch_size, epochs=5,
    validation_data=valid_generator.generate(), validation_steps=len(data_valid)//batch_size)

    # model.fit(data_train, rating_list_train, batch_size=batch_size, epochs=10, validation_data=(data_valid, rating_list_valid))

    score = model.evaluate_generator(test_generator.generate(), steps = len(data_test) // batch_size)

    model.save('model.h5')

    # score = model.evaluate(data_test, rating_list_test, batch_size=batch_size)

    print('Test Loss: ', score[0])
    print('Test Accuracy: ', score[1])

def build_vocab(filename, size):
    with tf.io.gfile.GFile(filename, "rb") as f:
        words =  f.read().decode("utf-8").split()
        words.insert(0, "<unk>")
        word_to_id = dict(zip(words[:size], range(size)))
        return word_to_id

def read_words(path, filename):
    with tf.io.gfile.GFile(path + filename, "rb") as f:
        # split file based on space characters and punctuation below
        return re.findall(r"[\w']+|[.\",!?;:]", f.read().decode('utf-8'))

def to_id(data, dictionary):
    for i in range(len(data)):
        data[i] = [dictionary[x] if x in dictionary else 0 for x in data[i]]
    return data

class AccHistory(keras.callbacks.Callback):
    def on_train_begin(self, logs={}):
        self.acc = []
    def on_epoch_end(self, batch, logs={}):
        self.acc.append(logs.get("acc"))


class batch_Generator(object):
    def __init__(self, input, labels, batch_size):
        self.data = input
        self.labels = labels
        self.batch_size = batch_size

        self.pointer = 0

    def generate(self):
        x = np.zeros((self.batch_size, 2540))
        y = np.zeros((self.batch_size, 2))

        while True:
            if self.pointer + self.batch_size > len(self.data):
                self.pointer = 0

            x = self.data[self.pointer : self.pointer + self.batch_size]
            y = self.labels[self.pointer : self.pointer + self.batch_size]

            self.pointer += self.batch_size

            yield x, y

if __name__ == "__main__":
    main()

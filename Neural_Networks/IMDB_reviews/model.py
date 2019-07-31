import keras
import tensorflow as tf
import numpy as np
import os
import string
import re

data_path_train_pos = "C:\\Users\Buddy\Documents\Programs\ProgrammingExersizes\\Neural_Networks\IMDB_reviews\\aclImdb\\train\pos\\"
data_path_train_neg = "C:\\Users\Buddy\Documents\Programs\ProgrammingExersizes\\Neural_Networks\IMDB_reviews\\aclImdb\\train\\neg\\"
data_path_test_pos = "C:\\Users\Buddy\Documents\Programs\ProgrammingExersizes\\Neural_Networks\IMDB_reviews\\aclImdb\\test\pos\\"
data_path_test_neg = "C:\\Users\Buddy\Documents\Programs\ProgrammingExersizes\\Neural_Networks\IMDB_reviews\\aclImdb\\test\\neg\\"
vocab_path = "C:\\Users\Buddy\Documents\Programs\ProgrammingExersizes\\Neural_Networks\IMDB_reviews\\aclImdb\imdb.vocab"

batch_size = 128

def main():
    # create dict from provided vocab file so that each word has a unique id
    vocab = build_vocab(vocab_path)
    vocab_size = len(vocab)

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

    reversed_vocab = dict(zip(vocab.values(), vocab.keys()))

    # get the rating of each review from the filename
    rating_list_train = [x[x.find('_')+1:x.find('.')] for x in data_train_files]
    rating_list_test = [x[x.find('_')+1:x.find('.')] for x in data_test_files]

    # convert from string to int
    rating_list_train = [int(x) for x in rating_list_train]
    rating_list_test = [int(x) for x in rating_list_test]

    # convert to one-hot vector
    rating_list_train  = [x-1 for x in rating_list_train]
    rating_list_test  = [x-1 for x in rating_list_test]
    rating_list_train = keras.utils.to_categorical(rating_list_train, num_classes=10)
    rating_list_test = keras.utils.to_categorical(rating_list_test, num_classes=10)

    # create validation set labels
    rating_list_test = rating_list_test[:int(len(rating_list_test)/2)]
    rating_list_valid = rating_list_test[int(len(rating_list_test)/2):]

    rating_list_train = np.array(rating_list_train)
    rating_list_test = np.array(rating_list_test)
    rating_list_valid = np.array(rating_list_valid)

    max_len = max([len(x) for x in data_train])

    for x in range(len(data_train)):
        data_train[x] = data_train[x] + [0] * (max_len - len(data_train[x]))

    for x in range(len(data_test)):
        data_test[x] = data_test[x] + [0] * (max_len - len(data_test[x]))

    for x in range(len(data_valid)):
        data_valid[x] = data_valid[x] + [0] * (max_len - len(data_valid[x]))

    data_train = np.array(data_train)
    data_test = np.array(data_test)
    data_valid = np.array(data_valid)

    # initialize the callback class
    hist = AccHistory()

    model = keras.Sequential()

    model.add(keras.layers.Embedding(vocab_size, 500, input_length=max_len))

    model.add(keras.layers.LSTM(500, return_sequences=True))
    model.add(keras.layers.LSTM(500))

    model.add(keras.layers.Dense(10, activation='softmax'))

    model.compile(optimizer='Adam', loss = 'categorical_crossentropy',

    metrics=['categorical_accuracy'])

    print(data_train.shape)
    print(rating_list_train.shape)
    model.fit(data_train, rating_list_train, batch_size=batch_size, epochs=10, callbacks=[hist], validation_data=(data_valid, rating_list_valid))

    score = model.evaluate(data_test, rating_list_test, batch_size=batch_size)

    print('Test Loss: ', score[0])
    print('Test Accuracy: ', score[1])

def build_vocab(filename):
    with tf.io.gfile.GFile(filename, "rb") as f:
        words =  f.read().decode("utf-8").split()
        words.insert(0, "<unk>")
        word_to_id = dict(zip(words, range(len(words))))
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
    def on_epoch_end(self, logs={}):
        self.acc.append(logs.get("acc"))




if __name__ == "__main__":
    main()

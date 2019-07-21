from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf

data_path = 'data\\fashion'
batch_size = 10
num_epoch = 20

bslist = [10, 50, 100, 200, 400, 1000, 2000] # best 10
lrlist = [.1, .05, .01, .005, .001, .0005, .0001] # best .0005
epochlist = [5, 10, 20, 40, 100] # best 20
# acc .8991
# can do hidden size and num of layers later

data = input_data.read_data_sets(data_path, one_hot=True)

def DNN():
    # intialize model with lr of .0005
    model = DNNModel(.0005)

    with tf.Session() as sess:
        # initialize graph
        sess.run(model.init)

        num_batches = len(data.train.images) // batch_size
        # run through the dataset num_epoch number of times
        for epoch in range(num_epoch):
            avg_cost = 0
            for batch in range(num_batches):
                # get the next batch
                train_x, train_y = data.train.next_batch(batch_size)
                # train the model
                _, cost = sess.run([model.optimizer, model.cost],
                    feed_dict={model.x : train_x, model.y : train_y})
                # calculate the average cost per epoch
                avg_cost += cost / num_batches

            # calculate the accuracy afer each epoch
            acc = sess.run([model.accuracy], feed_dict={model.x : data.test.images, model.y : data.test.labels})[0]
            print("Epoch {:.3f} Average Cost: {:.3f}".format(epoch+1, avg_cost))
            print("Epoch {:.3f} Accuracy: {:.3f}".format(epoch+1, acc))

        print("Training Finished")
        print("Final Accuracy: {}".format(acc))

# brute force regularisation using the list of parameters above
def select_paramsDNN():
    bestAcc = 0
    bestParams = {'BatchSize':0, 'LearningRate':0, 'NumEpochs':0}


    for bs in bslist:
        for lr in lrlist:
            for ep in epochlist:
                tf.reset_default_graph()
                with tf.Session() as sess:
                    model = DNNModel(lr)
                    sess.run(model.init)

                    num_batches = len(data.train.images) // bs
                    for epoch in range(ep):
                        avg_cost = 0
                        for batch in range(num_batches):
                            train_x, train_y = data.train.next_batch(batch_size)
                            _, cost = sess.run([model.optimizer, model.cost],
                                feed_dict={model.x : train_x, model.y : train_y})
                            avg_cost += cost / num_batches

                    accuracy = sess.run([model.accuracy], feed_dict={model.x : data.test.images, model.y : data.test.labels})

                    if accuracy[0] > bestAcc:
                        bestAcc = accuracy
                        bestParams['BatchSize'] = bs
                        bestParams['LearningRate'] = lr
                        bestParams['NumEpochs'] = ep

                    print("Training Finished")
                    print("Batch Size: {}, Learning Rate: {}, NumEpochs: {}".format(bs, lr, ep))
                    print("Final Accuracy: {}".format(accuracy[0]))
                    print("Final Average Cost: {}".format(avg_cost))
                    print("------------------------------------------------------------")

    print('Best Accuracy: {}'.format(bestAcc))
    print('Best Parameters:\n{}: {}\n{}: {}\n{}: {}\n'.format('BatchSize', bestParams['BatchSize'],
        'LearningRate', bestParams['LearningRate'], 'NumEpochs', bestParams['NumEpochs']))


class DNNModel():
    def __init__(self, lr):
        # 28 x 28 image, flattened to 784
        self.x = tf.placeholder(tf.float32, shape=[None, 784])
        self.y = tf.placeholder(tf.float32, shape=[None, 10])

        # hidden layer of 400 nodes
        self.w1 = tf.Variable(tf.random.normal([784, 400], stddev=.05))
        self.b1 = tf.Variable(tf.random.normal([400], stddev=.05))
        self.hidden_out = tf.nn.relu(tf.add(tf.matmul(self.x, self.w1), self.b1))

        # 10 node output layer
        self.w2 = tf.Variable(tf.random.normal([400, 10], stddev=.05))
        self.b2 = tf.Variable(tf.random.normal([10], stddev=.05))
        self.hidden_out2 = tf.add(tf.matmul(self.hidden_out,self. w2), self.b2)
        # the prediction
        self.softmax = tf.nn.softmax(self.hidden_out2)

        self.cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=self.hidden_out2, labels=self.y))

        self.optimizer = tf.train.AdamOptimizer(learning_rate= lr).minimize(self.cost)

        # argmax because softmax returns probabilities
        self.correct = tf.equal(tf.argmax(self.y, 1), tf.argmax(self.softmax, 1))
        self.accuracy = tf.reduce_mean(tf.cast(self.correct, dtype=tf.float32))

        self.init = tf.global_variables_initializer()

class CNNModel():
    def __init__(self):
        self.x = tf.placeholder(tf.float32, shape = [None, 784])
        self.y = tf.placeholder(tf.float32, shape = [None, 10])

        # data needs to be 4d,
        # -1: number of samples, dynamically reshaping
        # 28,28: mnist image 28 x 28 image
        # 1: single channel image, greyscale
        self.x_reshaped = tf.reshape(self.x, [-1, 28, 28, 1])

    def new_conv_layer(self, data, num_channels, num_filters, filter_shape, pool_shape, name):
        filter_shape = [filter_shape[0], filter_shape[1], num_channels, num_filters]

        return layer

if __name__ == "__main__":
    choice = int(input('1. DNN\n2. DNN Select Parameters\n'))
    if choice == 1:
        DNN()
    elif choice == 2:
        select_paramsDNN()

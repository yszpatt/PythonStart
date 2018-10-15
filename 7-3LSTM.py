import tensorflow as tf
import input_data

mnist = input_data.read_data_sets('MNIST_data', one_hot=True)

n_inputs = 28
max_time = 28
lstm_size = 100
n_classes = 10
batch_size = 100
n_batch = mnist.train.num_examples // batch_size

x = tf.placeholder(tf.float32, [None, 784])
y = tf.placeholder(tf.float32, [None, 10])

weights = tf.Variable(tf.truncated_normal([lstm_size, n_classes], stddev=0.1))
biases = tf.Variable(tf.constant(0.1, shape=[n_classes]))


def RNN(X, weights, biases):
    inputs = tf.reshape(X, [-1, max_time, n_inputs])
    lstm_cell = tf.contrib.rnn.BasicLSTMCell(lstm_size)
    outputs, final_state = tf.nn.dynamic_rnn(
        lstm_cell, inputs, dtype=tf.float32)
    results = tf.nn.softmax(tf.matmul(final_state[1], weights) + biases)
    return results

prediction = RNN(x, weights, biases)
corss_entropy = tf.reduce_mean(
    tf.nn.softmax_cross_entropy_with_logits(logits=prediction, labels=y))
train_step = tf.train.AdamOptimizer(1e-4).minimize(corss_entropy)
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(prediction, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for epoch in range(21):
        for batch in range(n_batch):
            batch_xs, batch_ys = mnist.train.next_batch(batch_size)
            sess.run(train_step, feed_dict={
                     x: batch_xs, y: batch_ys})
        acc = sess.run(accuracy, feed_dict={
            x: mnist.test.images[:1000], y: mnist.test.labels[:1000]})
        print("Iter" + str(epoch) + ".Test accuracy " + str(acc))

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

x_data = np.linspace(-0.5, 0.5, 200)[:, np.newaxis]
noise = np.random.normal(0, 0.01, x_data.shape)
y_data = np.square(x_data) + noise



x = tf.placeholder(tf.float32, x_data.shape)
y = tf.placeholder(tf.float32, y_data.shape)

# Weights_L1 = tf.Variable(tf.random_normal([1, 10]))
# biases_L1 = tf.Variable(tf.zeros([1, 10]))
# Wx_plus_b_L1 = tf.matmul(x, Weights_L1) + biases_L1
# L1 = tf.nn.tanh(Wx_plus_b_L1)

L1 = tf.layers.dense(x, 10, tf.nn.tanh) 


# Weights_L2 = tf.Variable(tf.random_normal([10, 1]))
# biases_L2 = tf.Variable(tf.zeros([1, 1]))
# Wx_plus_b_L2 = tf.matmul(L1, Weights_L2) + biases_L2
# prediction = Wx_plus_b_L2

prediction = tf.layers.dense(L1,1)


# loss = tf.reduce_mean(tf.square(y - prediction))
loss = tf.losses.mean_squared_error(y, prediction)
optimizer = tf.train.GradientDescentOptimizer(0.2)
train_op = optimizer.minimize(loss)
init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    for step in range(2000):
        # sess.run(train_op, feed_dict={x: x_data, y: y_data})
        _,l, prediction_value = sess.run(
            [train_op,loss, prediction], feed_dict={x: x_data, y: y_data})
    # plt.figure()
        if step % 20 == 0:
            plt.cla()
            plt.scatter(x_data, y_data)
            plt.plot(x_data, prediction_value, 'r-', lw=5)
            plt.text(0, 0, 'Loss=%.4f' %
                     l, fontdict={'size': 20, 'color': 'red'})
            plt.pause(0.1)
    plt.ioff()
    plt.show()

# for step in range(2000):
#     # train and net output
#     _, l, pred = sess.run([train_op, loss, output], {tf_x: x, tf_y: y})
#     if step % 5 == 0:
#         # plot and show learning process
#         plt.cla()
#         plt.scatter(x, y)
#         plt.plot(x, pred, 'r-', lw=5)
#         # plt.text(0.5, 0, 'Loss=%.4f' %
#         #          l, fontdict={'size': 20, 'color': 'red'})
#         plt.pause(0.1)

# plt.ioff()
# plt.show()

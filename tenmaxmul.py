#!/usr/bin/env python
# coding:utf-8

import tensorflow as tf
import input_data


import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = '1'  # 消息级别
os.environ["CUDA_VISIBLE_DEVICES"] = '0'  # 指定第一块GPU可用

config = tf.ConfigProto()
config.gpu_options.per_process_gpu_memory_fraction = 0.9  # 程序最多只能占用指定gpu的显存
config.gpu_options.allow_growth = True  # 程序按需申请内存
config.allow_soft_placement = True

mnist = input_data.read_data_sets('MNIST_data', one_hot=True)


def add_layer(inputs, in_size, out_size, activation_function=None):
    # addlayer
    Weights = tf.Variable(tf.random_normal([in_size, out_size]))
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)
    Wx_plus_b = tf.matmul(inputs, Weights) + biases

    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs


def compute_accuracy(v_xs, v_ys):
    # define out put
    global prediction
    y_pre = sess.run(prediction, feed_dict={xs: v_xs, keep_prob: 1})
    correct_prediction = tf.equal(tf.argmax(y_pre, 1), tf.argmax(v_ys, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    result = sess.run(accuracy, feed_dict={xs: v_xs, ys: v_ys, keep_prob: 1})
    return result


def weight_variable(shape):
    inital = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(inital)


def biase_variable(shape):
    inital = tf.constant(0.1, shape=shape)
    return tf.Variable(inital)


def conv2d(x, W):
    # define network layer
    # stride [1,x_movement,y_movement,1]
    # stride[0] = stride[4] = 1
    return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')


def max_pool_2x2(x):
    # polling
    # stride[0] = stride[4] = 1
    return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')


# define placeholder for inputs 28*28=784


xs = tf.placeholder(tf.float32, [None, 784])
ys = tf.placeholder(tf.float32, [None, 10])
keep_prob = tf.placeholder(tf.float32)

# change to shape
x_image = tf.reshape(xs, [-1, 28, 28, 1])
# print(x_image.shape)  #[n_samples,28,28,1]

# add output layer
# conv1 layer
W_conv1 = weight_variable([5, 5, 1, 32])  # patch:5x5  insize:1  outsize:32
b_conv1 = biase_variable([32])
h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) +
                     b_conv1)  # output size : 28 * 28 * 32
h_pool1 = max_pool_2x2(h_conv1)  # output size : 14 *14 *32

# conv2 layer
W_conv2 = weight_variable([5, 5, 32, 64])  # patch:5x5  insize:32  outsize:64
b_conv2 = biase_variable([64])
h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) +
                     b_conv2)  # output size : 14 * 14 * 64
h_pool2 = max_pool_2x2(h_conv2)  # output size : 7 *7 *64

# func1 layer
W_fc1 = weight_variable([7 * 7 * 64, 1024])
b_fc1 = biase_variable([1024])
# [n_samples,7,7,64] ->> [n_samples,7*7*64]
h_pool2_flat = tf.reshape(h_pool2, [-1, 7 * 7 * 64])
h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)
h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

# func2 layer
W_fc2 = weight_variable([1024, 10])
b_fc2 = biase_variable([10])
prediction = tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2)

# loss
cross_entropy = tf.reduce_mean(-tf.reduce_sum(ys *
                                              tf.log(prediction), reduction_indices=[1]))
train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)

# gpu_options = tf.GPUOptions(allow_growth=True)
sess = tf.Session(config=config)
sess.run(tf.global_variables_initializer())


for i in range(1000):
    # 100data
    batch_xs, batch_ys = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={
             xs: batch_xs, ys: batch_ys, keep_prob: 1})
    if i % 50 == 0:
        print(compute_accuracy(
            mnist.test.images[:1000], mnist.test.labels[:1000]))

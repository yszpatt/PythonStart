import tensorflow as tf
import input_data

mnist = input_data.read_data_sets('MNIST_data', one_hot=True)
# 数据批次
batch_size = 100
n_batch = mnist.train.num_examples // batch_size

x = tf.placeholder(tf.float32, [None, 784])
y = tf.placeholder(tf.float32, [None, 10])

# l1 = tf.layers.dense(x, 10, tf.nn.tanh)
# l1 = tf.layers.dense(x, 20, tf.nn.relu)
output = tf.layers.dense(x, 10, tf.nn.softmax)

# Weights_L1 = tf.Variable(tf.zeros([784, 10]))
# biases_L1 = tf.Variable(tf.zeros([10]))
# output = tf.nn.softmax(tf.matmul(x, Weights_L1) + biases_L1)

# 线性激励函数使用二次代价函数
# loss = tf.losses.mean_squared_error(y, output)

# S型激励函数使用交叉熵求平均
# loss = tf.reduce_mean(
#     tf.nn.softmax_cross_entropy_with_logits(labels=y, logits=output))
loss = tf.losses.softmax_cross_entropy(y, output)

# （对数释然函数）
# loss = tf.reduce_mean(-tf.reduce_sum(y *
#                                      tf.log(output), reduction_indices=[1]))


# 梯度下降
train_op = tf.train.GradientDescentOptimizer(0.3).minimize(loss)
# train_op = tf.train.AdamOptimizer(1e-2).minimize(loss)


init = tf.global_variables_initializer()

# 用于检测测试数据是否正确的bool
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(output, 1))
# bool列表转换为float32格式
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

saver = tf.train.Saver()

with tf.Session() as sess:
    sess.run(init)
    for step in range(11):
        for batch in range(n_batch):
            batch_xs, batch_ys = mnist.train.next_batch(batch_size)
            sess.run(train_op, feed_dict={
                x: batch_xs, y: batch_ys})
        acc = sess.run(accuracy, feed_dict={
            x: mnist.test.images[:1000], y: mnist.test.labels[:1000]})
        print("Iter" + str(step) + ".Test accuracy " + str(acc))
    saver.save(sess, 'net/mynet.ckpt')

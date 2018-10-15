import tensorflow as tf
import input_data

mnist = input_data.read_data_sets('MNIST_data', one_hot=True)
# 数据批次
batch_size = 100
n_batch = mnist.train.num_examples // batch_size

with tf.name_scope('input'):
    x = tf.placeholder(tf.float32, [None, 784], name='x_input')
    y = tf.placeholder(tf.float32, [None, 10], name='y_input')
keep_prob = tf.placeholder(tf.float32)
lr = tf.Variable(0.001, dtype=tf.float32)

with tf.name_scope('layer'):
    # l1 = tf.layers.dense(x, 10, tf.nn.tanh)
    l1 = tf.layers.dense(x, 200, tf.nn.tanh, name='layer1.tanh')
    l1_dropout = tf.nn.dropout(l1, keep_prob)
    # l2 = tf.layers.dense(l1_dropout, 200, tf.nn.tanh)
    output = tf.layers.dense(
        l1_dropout, 10, tf.nn.softmax, name='layer2.softmax')

# Weights_L1 = tf.Variable(tf.zeros([784, 10]))
# biases_L1 = tf.Variable(tf.zeros([10]))
# output = tf.nn.softmax(tf.matmul(x, Weights_L1) + biases_L1)

# 线性激励函数使用二次代价函数
# loss = tf.losses.mean_squared_error(y, output)

# S型激励函数使用交叉熵求平均
loss = tf.reduce_mean(
    tf.nn.softmax_cross_entropy_with_logits(labels=y, logits=output))
# loss = tf.losses.softmax_cross_entropy(y, output)

# （对数释然函数）
# loss = tf.reduce_mean(-tf.reduce_sum(y *
# tf.log(output), reduction_indices=[1]))


# 梯度下降
# train_op = tf.train.GradientDescentOptimizer(0.3).minimize(loss)
# train_op = tf.train.AdamOptimizer(lr).minimize(loss)
train_op = tf.train.MomentumOptimizer(0.1, 0.5).minimize(loss)
# train_op = tf.train.AdadeltaOptimizer(0.1).minimize(loss)

init = tf.global_variables_initializer()

# 用于检测测试数据是否正确的bool
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(output, 1))
# bool列表转换为float32格式
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

with tf.Session() as sess:
    sess.run(init)
    writer = tf.summary.FileWriter('logs/', sess.graph)
    for step in range(21):
        sess.run(tf.assign(lr, 0.001 * (0.95**step)))
        for batch in range(n_batch):
            batch_xs, batch_ys = mnist.train.next_batch(batch_size)
            sess.run(train_op, feed_dict={
                x: batch_xs, y: batch_ys, keep_prob: 1.0})
        test_acc = sess.run(accuracy, feed_dict={
            x: mnist.test.images[:1000], y: mnist.test.labels[:1000], keep_prob: 1.0})
        train_acc = sess.run(accuracy, feed_dict={
            x: mnist.train.images[:1000], y: mnist.train.labels[:1000], keep_prob: 1.0})
        print("Iter" + str(step) + ".Test accuracy " +
              str(test_acc) + ".Train accuracy" + str(train_acc))

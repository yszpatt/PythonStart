import tensorflow as tf

a = tf.constant([[3, 3]])
b = tf.constant([[2], [3]])

product = tf.matmul(a, b)
print(product)
sess = tf.Session()
print(sess)
result = sess.run(product)
print(result)
sess.close()

with tf.Session() as sess:
    result = sess.run(product)
    print(result)
